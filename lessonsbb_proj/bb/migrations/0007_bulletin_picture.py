# Generated by Django 4.2.11 on 2024-06-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0006_bulletin_create_timestamp_bulletin_update_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletin',
            name='picture',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Изображение'),
        ),
    ]