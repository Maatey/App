from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView

from app.models import Project, Topic, Question, Answer


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description"
        ]


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            "title",
            "text",
            "status",
            "author",
            "is_published",
            # "project",
            # "marked",
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            "title",
            "text",
            "status",
            # "project",
            # "marked",
        ]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            "description",
            "is_published",
        ]