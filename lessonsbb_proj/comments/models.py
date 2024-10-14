from django.db import models
from bb.models import Bulletin as BulletinModel

class Comment(models.Model):
    bb = models.ForeignKey(
        BulletinModel,
        verbose_name="Объявление",
        on_delete=models.CASCADE,
        related_name='comments',
        related_query_name='comments',
    )
    comment = models.TextField(
        verbose_name="Текст комментария"
    )
    create_timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Метка даты/времени создания записи",
        blank=True
    )
    update_timestamp = models.DateTimeField(
        auto_now=True,
        verbose_name="Метка даты/времени изменения записи",
        blank=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
