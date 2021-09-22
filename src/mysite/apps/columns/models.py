from django.db import models

from boards.models import Board


class Column(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="column", null=True)
    column_title = models.CharField('Name of title', max_length=200)

    def __str__(self):
        return self.column_title

    class Meta:
        verbose_name = 'Колонка'
        verbose_name_plural = 'Колонки'
