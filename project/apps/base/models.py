from django.contrib.staticfiles.views import serve
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


def validate_non_negative(value):
    if value < 0:
        raise ValueError(_('Значение не может быть отрицательным.'))


def validate_higher_value(value):
    if value > 10:
        raise ValueError(_('Значение не может быть больше 10.'))



class User(AbstractUser):
    username = models.CharField(max_length=256, null=True)
    email = models.EmailField(unique=True, null=True)
    login = models.CharField(max_length=256, null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars', default="assets/img/icons/avatar.svg")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = ['username', 'login', 'email', 'avatar', 'created', 'updated', 'id']
    SearchableFields = ['id', 'username', 'login', 'email', 'avatar', 'created', 'updated']
    FilterFields = ['created', 'updated']

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['-id', '-updated']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username or self.email


class Answers(models.Model):
    answer = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = ['id', 'answer', 'description', 'created', 'updated']
    SearchableFields = DisplayFields
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['-id', '-updated']
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.answer


class Questions(models.Model):
    question = models.TextField(blank=True, null=True)
    answers = models.ManyToManyField(Answers, related_name='r_answers', blank=True, db_index=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = ['id', 'question', 'created', 'updated']
    SearchableFields = DisplayFields
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['id', '-updated']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question
    

class Results(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    count = models.DecimalField(
        max_digits=100,
        decimal_places=0,
        blank=True, null=True,
        validators=[validate_non_negative]
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = ['id', 'questions', 'answer', 'count', 'created', 'updated']
    SearchableFields = DisplayFields
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['id', '-updated']
        verbose_name = 'Result'
        verbose_name_plural = 'Results'

    def __str__(self):
        return self.questions
    

class Reports(models.Model):
    csv = models.FileField(null=True, blank=True)
    graphic = models.ImageField(default='avatar.svg', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = ['id', 'csv', 'graphic', 'created', 'updated']
    SearchableFields = DisplayFields
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['id', '-updated']
        verbose_name = 'Reports'
        verbose_name_plural = 'Reports'

    def __str__(self):
        return f"Отчет №{self.id}"
