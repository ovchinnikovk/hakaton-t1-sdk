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


@admin.register(models.Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = models.Results.DisplayFields
    search_fields = models.Results.SearchableFields
    list_filter = models.Results.FilterFields


@admin.register(models.Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_display = models.Reports.DisplayFields
    search_fields = models.Reports.SearchableFields
    list_filter = models.Reports.FilterFields
