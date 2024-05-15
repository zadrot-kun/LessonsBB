from django.shortcuts import render
from django.views.generic.edit import CreateView
from bb.models import Bulletin as BulletinModel, Rubric as RubricModel
from bb.forms import BBForm, RubricForm
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.urls import reverse


class CreateRubricController(CreateView):
    model = RubricModel
    form_class = RubricForm
    template_name = "bb/new_record.html"

    def get_success_url(self):
        return reverse('index')


class CreateBBController(CreateView):
    model = BulletinModel
    form_class = BBForm
    template_name = "bb/new_record.html"

    def get_success_url(self):
        return reverse('index')


def rubric_list(request):
    all_rubrics = [{'id': x.pk, 'name': x.name, 'parent': str(x.parent)} for x in RubricModel.objects.all()]
    return JsonResponse(all_rubrics, safe=False)


def index(request):
    rubrics = RubricModel.objects.all()
    bbs = BulletinModel.objects.all()
    return TemplateResponse(request,
                            'bb/index.html',
                            context={"rubrics": rubrics,
                                     "bbs": bbs})


def index_by_rubric(request, rubric):
    rubrics = RubricModel.objects.all()
    bbs = BulletinModel.objects.filter(rubric=rubric)
    return TemplateResponse(request,
                            'bb/index.html',
                            context={"rubrics": rubrics,
                                     "bbs": bbs})
