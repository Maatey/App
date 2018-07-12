from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, update_session_auth_hash
from .forms import SignupForm, ProjectForm, QuestionForm, AnswerForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from app.models import Project, Topic, Question, Answer


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('registration/account_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


# main
def main_view(request):
    projects = Project.objects.all()
    topics = Topic.objects.all()
    questions = Question.objects.all()
    context = {
        "title": "Projects",
        "title_pro": projects.model.__name__,
        "title_top": topics.model.__name__,
        "title_que": questions.model.__name__,
    }
    return render(request, "service/main.html", context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
    return super().get_redirect_url(*args, **kwargs)


class ProjectView(TemplateView):

    def get(self, request):
        queryset = Project.objects.all()
        context = {
            "title": "Projects",
            "object_list": queryset,
        }
        render(request, "get_project.html", context)

        if request.method == "GET":
            form = Question.objects.filter(project__id=1)
            context = {
                "instance": form,
            }
            render(request, "get_question.html", context)

            if request.method == "GET":
                form = Answer.objects.filter(question__id=1)
                context = {
                    "instance": form,
                }
                return render(request, "get_answer.html", context)


"""
class TopicView(TemplateView):

    def get(self, request):
        queryset = Project.objects.all()
        context = {
            "title": "Topics",
            "object_list": queryset,
        }
        return render(request, "index.html", context)


class QuestionView(TemplateView):

    def get(self, request):
        queryset = Question.objects.all()
        context = {
            "title": "Question",
            "object_list": queryset,
        }
        return render(request, "index.html", context)


class ProjectAddView(CreateView):
    template_name = "add.html"
    model = Project
    fields = ['title', 'description']
"""


# Projects


def get_project_detail(request, pk=None):
    instance = get_object_or_404(Project, pk=pk)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "get_project_detail.html", context)


def post_project(request):
    form = ProjectForm(request.POST or None)
    if request.method == 'POST':
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form,
    }
    return render(request, "post_project.html", context)


def get_project(request):
    queryset = Project.objects.all()
    context = {
        "title": "Projects",
        "object_list": queryset,
    }
    return render(request, "get_project.html", context)


def get_question(request, id=1):
    instance = Question.objects.filter(project__id=id)
    context = {
        "instance": instance,
    }
    return render(request, "get_question.html", context)


def get_answer(request, id=1):
    instance = Answer.objects.filter(question__id=id)
    context = {
        "instance": instance,
    }
    return render(request, "get_answer.html", context)


def post_answer(request, pk=None):
    instance = get_object_or_404(Answer, pk=pk)
    form = AnswerForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Created")
        return HttpResponseRedirect('/app/get_answer.html')
    else:
        messages.error(request, "Not Created!")
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_answer.html", context)


class ProjectView(TemplateView):

    template_name = "app/project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Project.objects.all()
        return context
