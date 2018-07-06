from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


