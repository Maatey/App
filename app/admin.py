from django.contrib import admin

# Register your models here.
from app.models import Project, UserAssign, Topic, Question, Answer


class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ["question", "author", "is_internal", "is_published", "published_time"]

    class Meta:
        model = Answer


class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class Meta:
        model = Project


class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "author", "is_published", "published_time"]

    class Meta:
        model = Question


class TopicModelAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "author", "is_published", "published_time"]

    class Meta:
        model = Topic

class UserAssignModelAdmin(admin.ModelAdmin):
    list_display = ["project", "user"]

    class Meta:
        model = UserAssign


admin.site.register(Answer, AnswerModelAdmin)
admin.site.register(Project, ProjectModelAdmin)
admin.site.register(Topic, TopicModelAdmin)
admin.site.register(Question, QuestionModelAdmin)
admin.site.register(UserAssign, UserAssignModelAdmin)

