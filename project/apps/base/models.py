from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


def validate_non_negative(value):
    if value < 0:
        raise ValueError(_('Баланс не может быть отрицательным.'))


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
    title = models.CharField(max_length=250, blank=True, null=True)
    answer = models.CharField(max_length=250, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = ['id', 'title', 'answer', 'created', 'updated']
    SearchableFields = DisplayFields
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['-id', '-updated']
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.answer


class Questions(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    number = models.DecimalField(
        max_digits=100,
        decimal_places=0,
        blank=True, null=True,
        validators=[validate_non_negative]
    )
    question = models.TextField(blank=True, null=True)
    answers = models.ManyToManyField(Answers, related_name='r_answers', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    DisplayFields = ['id', 'title', 'number', 'question', 'created', 'updated']
    SearchableFields = DisplayFields
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['id', '-updated']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question
