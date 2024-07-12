# Generated by Django 4.2.11 on 2024-07-12 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0009_alter_bulletin_rubric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='rubric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bbs', related_query_name='bbs', to='bb.rubric', verbose_name='Рубрика'),
        ),
    ]