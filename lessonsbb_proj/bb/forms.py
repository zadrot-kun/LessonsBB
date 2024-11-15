import django.forms as forms
from bb.models import Bulletin as BulletinModel, Rubric as RubricModel, Picture as PictureModel
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory

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

    # def clean_name (self):
    #     if 'Сергей' in self.cleaned_data["name"]:
    #         raise ValidationError("Не люблю Сергеев!")
    #     return self.cleaned_data["name"]
    #
    # def clean(self):
    #     super().clean()
    #     if (float(self.data["cost"]) > 1000000) and (self.data["curr"] == 'руб'):
    #         raise ValidationError("Чрезмерно высокая стоимость объявления")

    class Meta:
        model = BulletinModel
        # fields = ['name', 'description']
        fields = '__all__'
        # exclude = ('rubric', 'picture')

class PictureForm(forms.ModelForm):

    class Meta:
        model = PictureModel
        fields = '__all__'

BBFormSet = inlineformset_factory(
    BulletinModel,
    PictureModel,
    fields = '__all__'
)

class RubricForm(forms.ModelForm):
    class Meta:
        model = RubricModel
        fields = "__all__"
