from django.contrib import admin
from bb.models import Rubric, Bulletin


class ParentEditor(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_display_links = ('name', )


class BulletinEditor(admin.ModelAdmin):
    list_display = ('name', 'active_flag')
    list_display_links = ('name', )


admin.site.register(Rubric, ParentEditor)
admin.site.register(Bulletin, BulletinEditor)
