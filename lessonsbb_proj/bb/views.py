from django.shortcuts import render
from django.views.generic.edit import CreateView
from bb.models import Bulletin as BulletinModel, Rubric as RubricModel
from bb.forms import BBForm, RubricForm


class CreateRubricController(CreateView):
    model = RubricModel
    form_class = RubricForm
    template_name = "bb/new_rubric.html"
