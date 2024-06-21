# Generated by Django 4.2.11 on 2024-05-22 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0003_alter_rubric_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='rubric',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bb.rubric', verbose_name='Родительская рубрика'),
        ),
    ]