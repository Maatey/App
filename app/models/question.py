from django.contrib.auth import get_user_model
from django.db import models

from app.models import Topic, Project

User = get_user_model()


class Question(models.Model):
    NEW = 'NEW'
    IN_PROGRESS = 'INP'
    RESOLVED = 'RES'
    STATUS_CHOICES = (
        (NEW, 'New'),
        (IN_PROGRESS, 'In progress'),
        (RESOLVED, 'Resolved'),
    )
    title = models.CharField(max_length=64)
    text = models.TextField(max_length=255)
    author = models.ForeignKey(User, on_delete=False, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default=NEW, max_length=25)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    published_time = models.TimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __unicode__(self):
        return self.author
