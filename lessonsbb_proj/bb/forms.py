import django.forms as forms
from bb.models import Bulletin as BulletinModel, Rubric as RubricModel


class UpdateBulletinForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label = "Название",
    )
    description = forms.CharField(
        label="Описание",
        widget=forms.Textarea(),
    )

class BBForm(forms.ModelForm):
    class Meta:
        model = BulletinModel
        # fields = ['name', 'description']
        fields = '__all__'
        # exclude = ('rubric', 'picture')


class RubricForm(forms.ModelForm):
    class Meta:
        model = RubricModel
        fields = "__all__"
