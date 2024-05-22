from django.contrib import admin
from bb.models import Rubric


class ParentEditor(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_display_links = ('name', )


admin.site.register(Rubric, ParentEditor)
