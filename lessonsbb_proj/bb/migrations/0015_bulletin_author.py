# Generated by Django 4.2.14 on 2024-12-04 04:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bb', '0014_remove_bulletin_pictures_picture_bb_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletin',
            name='author',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]
