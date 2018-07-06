from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View


class LoginView(View):
    register_url = ''

    def post(self, request):
        return self._log_in(request)

    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        if request.GET.get('next'):
            next = request.GET.get('next')
        else:
            next = ''
        response = render(request, 'account/login.html',
                          {'next': next, 'register': self.register_url})
        response["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response["Pragma"] = "no-cache"
        return response

    def _log_in(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is None:
            return render(request, 'login.html', {
                'error_message': "Niepoprawne dane",
                'next': request.POST.get('next') if request.POST.get('next') else '',
                'register': self.register_url
            })

        if not user.is_active:
            return render(request, 'login.html', {
                'error_message': "Konto nieaktywne",
                'next': request.POST.get('next') if request.POST.get('next') else '',
                'register': self.register_url
            })

        login(request, user)

        if request.POST.get('next') != '':
            response = HttpResponseRedirect(request.POST.get('next'))
            return response
        else:
            response = HttpResponseRedirect('/home')
            return response


class ProfileView(View):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile.html'

    def get(self, request):
        profile = request.user
        return request({'user'})

    def post(self, request):
        user = request.user
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        return request({'user'})
