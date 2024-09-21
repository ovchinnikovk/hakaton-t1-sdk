from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = models.User.DisplayFields
    search_fields = models.User.SearchableFields
    list_filter = models.User.FilterFields


@admin.register(models.Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = models.Answers.DisplayFields
    search_fields = models.Answers.SearchableFields
    list_filter = models.Answers.FilterFields


@admin.register(models.Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = models.Questions.DisplayFields
    search_fields = models.Questions.SearchableFields
    list_filter = models.Questions.FilterFields
