from django.db import models


class Rubric(models.Model):
    """Модель рубрики"""
    name = models.CharField(max_length=100,
                            verbose_name="Название",
                            unique=True)
    parent = models.ForeignKey('self',
                               on_delete=models.SET_NULL,
                               verbose_name="Родительская рубрика",
                               null=True)


class Bulletin(models.Model):
    """Модель объявления"""
    name = models.CharField(max_length=100,
                            verbose_name="Название")
    description = models.TextField(verbose_name="Описание",
                                   help_text="Текст неограниченной длинны")
    cost = models.DecimalField(decimal_places=2, max_digits=11)
    curr = models.CharField(max_length=3,
                            verbose_name="Валюта")
    rubric = models.ForeignKey(Rubric,
                               on_delete=models.PROTECT,
                               verbose_name="Рубрика")
