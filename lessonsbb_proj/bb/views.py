from django.shortcuts import render
from django.views.generic.edit import CreateView
from bb.models import Bulletin as BulletinModel, Rubric as RubricModel
from bb.forms import BBForm, RubricForm
from django.http import JsonResponse
from django.template.response import TemplateResponse


class CreateRubricController(CreateView):
    model = RubricModel
    form_class = RubricForm
    template_name = "bb/new_rubric.html"


def rubric_list(request):
    all_rubrics = [{'id': x.pk, 'name': x.name, 'parent': str(x.parent)} for x in RubricModel.objects.all()]
    return JsonResponse(all_rubrics, safe=False)


def index(request):
    return TemplateResponse(request, 'bb/index.html', context={"rubrics": RubricModel.objects.all()})
