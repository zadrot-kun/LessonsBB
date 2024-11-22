# Generated by Django 4.2.14 on 2024-10-14 04:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='create_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 10, 14, 4, 52, 21, 782530, tzinfo=datetime.timezone.utc), verbose_name='Метка даты/времени создания записи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='update_timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='Метка даты/времени изменения записи'),
        ),
    ]