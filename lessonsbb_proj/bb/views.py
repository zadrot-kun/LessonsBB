from django.shortcuts import render
from django.views.generic.edit import CreateView
from bb.models import Bulletin as BulletinModel, Rubric as RubricModel
from bb.forms import BBForm, RubricForm
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.urls import reverse
from django.http import HttpResponseRedirect


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
