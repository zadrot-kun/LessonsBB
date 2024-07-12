from django.db import models
from django.core import validators

min_10_chars_vlid = validators.MinLengthValidator(
    10,
    message='Значение не может быть меньше 10 символов')


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
                            verbose_name="Название",
                            validators=[min_10_chars_vlid])
    description = models.TextField(verbose_name="Описание",
                                   help_text="Текст неограниченной длинны",
                                   validators=[min_10_chars_vlid])
    cost = models.DecimalField(decimal_places=2, max_digits=11)
    curr = models.CharField(max_length=3,
                            verbose_name="Валюта")
    rubric = models.ForeignKey(Rubric,
                               on_delete=models.PROTECT,
                               verbose_name="Рубрика",
                               related_name='bbs',
                               related_query_name='bbs')
    create_timestamp = models.DateTimeField(auto_now_add=True,
                                            verbose_name="Метка даты/времени создания записи",
                                            blank=True)
    update_timestamp = models.DateTimeField(auto_now=True,
                                            verbose_name="Метка даты/времени изменения записи",
                                            blank=True)
    picture = models.ImageField(verbose_name="Изображение",
                                upload_to="img",
                                blank=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-rubric', '-cost']
        unique_together = ('name', 'description', 'cost')
        permissions = (
            ('alcohol', 'Права на покупку алкоголя'),
        )
        default_permissions = ('add', 'view', 'change', 'delete', 'alcohol')
