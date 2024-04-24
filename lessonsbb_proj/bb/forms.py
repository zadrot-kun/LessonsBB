from django.forms import ModelForm
from bb.models import Bulletin as BulletinModel, Rubric as RubricModel


class BBForm(ModelForm):
    class Meta:
        model = BulletinModel
        fields = "__all__"


class RubricForm(ModelForm):
    class Meta:
        model = RubricModel
        fields = "__all__"
