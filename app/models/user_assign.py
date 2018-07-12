from django.contrib.auth import get_user_model
from django.db import models

from app.models.project import Project

User = get_user_model()


class UserAssign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_project')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='user_assign')
    is_project_lead = models.BooleanField(default=False)
