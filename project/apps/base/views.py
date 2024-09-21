from django.shortcuts import render
from . import models

def main(request):
    questions = models.Questions.objects.all()

    context = {'questions': questions}
    return render(request, template_name='base/main.htm', context=context)
