# Generated by Django 4.2.14 on 2024-10-14 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0011_bulletin_active_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Стоимость'),
        ),
    ]