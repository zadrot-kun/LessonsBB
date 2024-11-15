from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from bb.models import Bulletin as BulletinModel, Rubric as RubricModel
from bb.forms import BBForm, RubricForm, UpdateBulletinForm, BBFormSet
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.db import models
from django.views.decorators.http import require_GET, require_http_methods
from django.views.generic.base import TemplateView
from django.forms import inlineformset_factory
from comments.models import Comment as CommentModel
from django.forms.widgets import TextInput


SORTING_DICT = {
    'name': "Название",
    'description': "Описание",
    'cost': "Стоимость",
    'rubric': "Рубрика",
    'create_timestamp': "Дата создания",
    'update_timestamp': "Дата обновления",
}


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
            bb_form.save()
            # new_bb = BulletinModel(name=bb_form.cleaned_data['name'],
            #                        description=bb_form.cleaned_data['description'],
            #                        cost=bb_form.cleaned_data['cost'],
            #                        curr=bb_form.cleaned_data['curr'],
            #                        rubric=bb_form.cleaned_data['rubric'],
            #                        picture=bb_form.cleaned_data['picture'])
            # new_bb.save()
            # new_bb.description += '!'
            # new_bb.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return TemplateResponse(request,
                                    template_name,
                                    context={'form': bb_form})


# @require_GET
@require_http_methods(['GET', 'POST'])
def update_bb(request, bb_pk):
    template_name = "bb/new_record.html"
    try:
        bb = BulletinModel.objects.get(pk=bb_pk)
    except BulletinModel.DoesNotExist:
        return HttpResponseNotFound('Не найдено данное объявление')
    if request.method == 'GET':
        # bb_form = UpdateBulletinForm(initial={'name': bb.name, 'description': bb.description,})
        bb_form = BBForm(instance=bb)
        bbimages_formset = BBFormSet(instance=bb)
        class_formset = inlineformset_factory(
            BulletinModel,
            CommentModel,
            fields=['comment'],
            extra=1,
            widgets={'comment': TextInput},
        )
        formset = class_formset(instance=bb)
        return TemplateResponse(
            request,
            template_name,
            context={
                'form': bb_form,
                'comment_formset': formset,
                'bb_pk': bb_pk,
                'images_formset': bbimages_formset,
            }
        )
    elif request.method == 'POST':
        bb_form = BBForm(request.POST, request.FILES, instance=bb)
        if bb_form.is_valid():
            bb_form.save()
            # bb.name = request.POST['name']
            # bb.description = bb_form.cleaned_data['description']
            # bb.cost = bb_form.cleaned_data['cost']
            # bb.curr = bb_form.cleaned_data['curr']
            # bb.rubric = bb_form.cleaned_data['rubric']
            # bb.picture = bb_form.cleaned_data['picture']
            # bb.save()
            # return HttpResponseRedirect(reverse('index'))
            return redirect(reverse('index'))
        else:
            return TemplateResponse(request,
                                    template_name,
                                    context={'form': bb_form})

@require_http_methods(['POST'])
def update_bb_comments(request, bb_pk):
    try:
        bb = BulletinModel.objects.get(pk=bb_pk)
    except BulletinModel.DoesNotExist:
        return HttpResponseNotFound('Не найдено данное объявление')
    if request.method == 'POST':
        class_formset = inlineformset_factory(BulletinModel, CommentModel, fields=['comment'], extra=1)
        bbimages_formset = BBFormSet(request.POST, instance=bb)
        if bbimages_formset.is_valid():
            bbimages_formset.save()
        return redirect(reverse('update_bb', kwargs={'bb_pk': bb_pk}))

@require_http_methods(['POST'])
def update_bb_images(request, bb_pk):
    try:
        bb = BulletinModel.objects.get(pk=bb_pk)
    except BulletinModel.DoesNotExist:
        return HttpResponseNotFound('Не найдено данное объявление')
    class_formset = inlineformset_factory(BulletinModel, CommentModel, fields=['comment'], extra=1)
    formset = class_formset(request.POST, request.FILES, instance=bb)
    if formset.is_valid():
        formset.save()
    return redirect(reverse('update_bb', kwargs={'bb_pk': bb_pk}))

class CreateBBController(CreateView):
    model = BulletinModel
    form_class = BBForm
    template_name = "bb/new_record.html"

    def get_success_url(self):
        return reverse('index')


def test_json_controller(request):
    all_data = [x.pk for x in BulletinModel.objects.order_by("rubric")]
    return JsonResponse(all_data, safe=False)


class IndexClass(TemplateView):

    template_name = 'bb/index.html'

    def get_context_data(self, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['rubrics'] = RubricModel.objects.annotate(count_bb=models.Count('bbs__pk'))
        bbs = BulletinModel.objects.all().annotate(cfield=models.functions.TruncTime('update_timestamp'))
        filter_dict = {}
        for filter_key in (x for x in self.request.GET if x.startswith('filter_')):
            if filter_key.endswith('__in'):
                filter_dict[filter_key[7:]] = self.request.GET[filter_key].split(',')
            else:
                filter_dict[filter_key[7:]] = self.request.GET[filter_key]
        if filter_dict:
            print(filter_dict)
            bbs = bbs.filter(**filter_dict)
        selected_order = ''
        if 'order' in self.request.GET:
            bbs = bbs.order_by(self.request.GET['order'])
            selected_order = self.request.GET['order']
        selected_rubric = ''
        if 'filter_rubric' in self.request.GET:
            selected_rubric = int(self.request.GET['filter_rubric'])
        context_dict["bbs"] = bbs
        context_dict["sorting_dict"] = SORTING_DICT
        context_dict['selected_order'] = selected_order
        context_dict['selected_rubric'] = selected_rubric
        return context_dict


def index(request):
    rubrics = RubricModel.objects.annotate(count_bb=models.Count('bbs__pk'))
    # rubrics = RubricModel.objects.annotate(count_bb=models.functions.NullIf('parent', models.Value(2)))
    # rubrics = RubricModel.objects.annotate(count_bb=models.functions.Now())
    # rubrics = RubricModel.objects.annotate(count_bb=models.Value('♥'))
    # rubrics = RubricModel.objects.annotate(count_bb=models.functions.Chr(models.Value(9829)))
    # rubrics = RubricModel.objects.annotate(count_bb=models.functions.Concat(models.Value('Название рубрики: '), models.F('name')))
    # rubrics = RubricModel.objects.annotate(count_bb=models.functions.Substr('name', 2, 2))
    # rubrics = RubricModel.objects.annotate(count_bb=models.functions.Length('name'))
    # rubrics = RubricModel.objects.annotate(count_bb=models.funct  ions.Replace('name', models.Value('о'), models.Value('!')))
    # rubrics_flag = {}
    # for rubric in rubrics:
    #     rubrics_flag[rubric.pk] = BulletinModel.objects.filter(rubric=rubric.pk).annotate(models.Count('pk'))['cost__avg']
    # -- выборка по подзапросу
    # nedv_rubrcs = RubricModel.objects.filter(models.Q(name='Недвижимость') | models.Q(parent__name='Недвижимость'))
    # subq_nedv_rubrcs = models.Subquery(nedv_rubrcs.values("pk"))
    # bbs = BulletinModel.objects.all().filter(rubric__in=subq_nedv_rubrcs)
    # bbs = BulletinModel.objects.all().annotate(cfield=models.functions.Trunc('update_timestamp', 'week'))
    # bbs = BulletinModel.objects.all().annotate(cfield=models.functions.TruncDate('update_timestamp'))
    # bbs = BulletinModel.objects.all().annotate(cfield=models.functions.TruncTime('update_timestamp'))
    bbs = BulletinModel.objects.all().annotate(cfield=models.functions.TruncTime('update_timestamp'))
    # test_list = [
    #     "Дома",
    #     "Мебель"
    # ]
    # print(rubrics)
    # rubrics = rubrics.in_bulk(test_list, field_name='name')
    # print(rubrics)
    # bbs = BulletinModel.objects.all().annotate(cfield=models.functions.Sqrt('cost'))
    # bbs = BulletinModel.objects.all().annotate(cfield=models.Case(
    #         models.When(create_timestamp__gt=models.F('update_timestamp'), then=models.F('create_timestamp')),
    #         models.When(update_timestamp__gt=models.F('create_timestamp'), then=models.F('update_timestamp')),
    #         default=None
    #     )
    # )
    # for x in bbs.values_list('id', 'description', 'cost', 'curr'):
    #     print(x)
    filter_dict = {}
    for filter_key in (x for x in request.GET if x.startswith('filter_')):
        if filter_key.endswith('__in'):
            filter_dict[filter_key[7:]] = request.GET[filter_key].split(',')
        else:
            filter_dict[filter_key[7:]] = request.GET[filter_key]
    if filter_dict:
        print(filter_dict)
        bbs = bbs.filter(**filter_dict)
    selected_order = ''
    if 'order' in request.GET:
        bbs = bbs.order_by(request.GET['order'])
        selected_order = request.GET['order']
    selected_rubric = ''
    if 'filter_rubric' in request.GET:
        selected_rubric = int(request.GET['filter_rubric'])
    return TemplateResponse(request,
                            'bb/index.html',
                            context={"rubrics": rubrics,
                                     "bbs": bbs,
                                     "sorting_dict": SORTING_DICT,
                                     'selected_order': selected_order,
                                     'selected_rubric': selected_rubric,
                                     # 'rubrics_flag': rubrics_flag
                                     }
                            )


def index_by_rubric(request, rubric):
    rubrics = RubricModel.objects.all()
    bbs = BulletinModel.objects.filter(rubric=rubric)
    return TemplateResponse(request,
                            'bb/index.html',
                            context={"rubrics": rubrics,
                                     "bbs": bbs})
