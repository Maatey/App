from django.contrib.auth import get_user_model
from django.db import models
from app.models import Project

User = get_user_model()


class Topic(models.Model):
    NEW = 'NEW'
    IN_PROGRESS = 'INP'
    RESOLVED = 'RES'
    STATUS_CHOICES = (
        (NEW, 'New'),
        (IN_PROGRESS, 'In progress'),
        (RESOLVED, 'Resolved'),
    )
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, default=NEW, max_length=3)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank = True)
    published_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    marked = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def __unicode__(self):
        return self.author
