from django.contrib.auth import get_user_model
from django.db import models

from app.models import Question

User = get_user_model()


class Answer(models.Model):
    description = models.TextField(max_length=255)
    is_published = models.BooleanField(default=False)
    is_internal = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True)
    published_time = models.DateTimeField(auto_now=False, auto_now_add=True)
