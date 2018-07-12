from django.db import models
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title