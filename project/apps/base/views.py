import json
from itertools import count

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models


def main(request):
    questions = models.Questions.objects.all()

    context = {'questions': questions}
    return render(request, template_name='base/main.htm', context=context)


@csrf_exempt
def post_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            selected_options = data.get('result')

            for question_id, answer in selected_options.items():
                question = models.Questions.objects.get(id=int(question_id))
                existing_model, created = models.Results.objects.get_or_create(
                    questions=question,
                    answer=answer,
                    defaults={'count': 1}
                )

                if not created:
                    existing_model.count += 1
                    existing_model.save()

            return JsonResponse({'success': True})
        except (ValueError, KeyError, models.Questions.DoesNotExist):
            return JsonResponse({'error': 'Invalid request data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
