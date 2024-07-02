from django.shortcuts import render
from django.views.generic.edit import CreateView
from bb.models import Bulletin as BulletinModel, Rubric as RubricModel
from bb.forms import BBForm, RubricForm
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.db import models


class CreateRubricController(CreateView):
    model = RubricModel
    form_class = RubricForm
    template_name = "bb/new_record.html"

    def get_success_url(self):
        return reverse('index')


def create_bb(request):
    template_name = "bb/new_record.html"
    if request.method == 'GET':
        bb_form = BBForm()
        return TemplateResponse(request,
                                template_name,
                                context={'form': bb_form})
    elif request.method == 'POST':
        bb_form = BBForm(request.POST, request.FILES)
        if bb_form.is_valid():
            # bb_form.save()
            new_bb = BulletinModel(name=bb_form.cleaned_data['name'],
                                   description=bb_form.cleaned_data['description'],
                                   cost=bb_form.cleaned_data['cost'],
                                   curr=bb_form.cleaned_data['curr'],
                                   rubric=bb_form.cleaned_data['rubric'],
                                   picture=bb_form.cleaned_data['picture'])
            new_bb.save()
            new_bb.description += '!'
            new_bb.save()
            return HttpResponseRedirect("/")
        else:
            return TemplateResponse(request,
                                    template_name,
                                    context={'form': bb_form})


def update_bb(request, bb_pk):
    template_name = "bb/new_record.html"
    try:
        bb = BulletinModel.objects.get(pk=bb_pk)
    except BulletinModel.DoesNotExist:
        return HttpResponseNotFound('Не найдено данное объявление')
    if request.method == 'GET':
        bb_form = BBForm(instance=bb)
        return TemplateResponse(request,
                                template_name,
                                context={'form': bb_form})
    elif request.method == 'POST':
        bb_form = BBForm(request.POST, request.FILES, instance=bb)
        if bb_form.is_valid():
            # bb_form.save()
            bb.name = request.POST['name']
            bb.description = bb_form.cleaned_data['description']
            bb.cost = bb_form.cleaned_data['cost']
            bb.curr = bb_form.cleaned_data['curr']
            bb.rubric = bb_form.cleaned_data['rubric']
            bb.picture = bb_form.cleaned_data['picture']
            bb.save()
            return HttpResponseRedirect("/")
        else:
            return TemplateResponse(request,
                                    template_name,
                                    context={'form': bb_form})

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
    # -- выборка по подзапросу
    # nedv_rubrcs = RubricModel.objects.filter(models.Q(name='Недвижимость') | models.Q(parent__name='Недвижимость'))
    # subq_nedv_rubrcs = models.Subquery(nedv_rubrcs.values("pk"))
    # bbs = BulletinModel.objects.all().filter(rubric__in=subq_nedv_rubrcs)
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
