from django.shortcuts import render
from . import models

def main(request):
    return render(request, template_name='base/main.htm', context={})
