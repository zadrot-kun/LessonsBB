from django.db import models


class Rubric(models.Model):
    """Модель рубрики"""
    name = models.CharField(max_length=100,
                            verbose_name="Название",
                            unique=True)
    parent = models.ForeignKey('self',
                               on_delete=models.SET_NULL,
                               verbose_name="Родительская рубрика",
                               null=True,
                               default=None,
                               blank=True)

    def name_length(self):
        return len(self.name)

    def __str__(self):
        return f"{self.name}({self.pk})"

    # def get_absolute_url(self):
    #     return "/bb/create_rubric/"

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['-name']


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

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-rubric', '-cost']
        unique_together = ('name', 'description', 'cost')
