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
    priority = models.DecimalField(
        max_digits=2,
        decimal_places=0,
        blank=True, null=True,
        validators=[validate_higher_value, validate_non_negative]
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = ['id', 'answer', 'description', 'priority', 'created', 'updated']
    SearchableFields = DisplayFields
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['-id', '-updated']
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.priority


class Questions(models.Model):
    number = models.DecimalField(
        max_digits=100,
        decimal_places=0,
        blank=True, null=True,
        validators=[validate_non_negative]
    )
    question = models.TextField(blank=True, null=True)
    answers = models.ManyToManyField(Answers, related_name='r_answers', blank=True)
    priority = models.DecimalField(
        max_digits=2,
        decimal_places=0,
        blank=True, null=True,
        validators=[validate_higher_value, validate_non_negative]
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = ['id', 'number', 'question', 'priority', 'created', 'updated']
    SearchableFields = DisplayFields
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['id', '-updated']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question
    

class Results(models.Model):
    option = models.CharField(max_length=250, blank=True, null=True)
    count = models.DecimalField(
        max_digits=100,
        decimal_places=0,
        blank=True, null=True,
        validators=[validate_non_negative]
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = ['id', 'option', 'count', 'created', 'updated']
    SearchableFields = DisplayFields
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['id', '-updated']
        verbose_name = 'Result'
        verbose_name_plural = 'Results'

    def __str__(self):
        return self.option
