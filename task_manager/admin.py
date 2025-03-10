from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task_manager.models import (
    Worker,
    Team,
    Position,
    Tag,
    TaskType,
    Project, Comment, Task
)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("team", "position")
    fieldsets = UserAdmin.fieldsets + (
        ("Team info", {"fields": ("team", "position")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Team info", {"fields": ("team", "position")})
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
