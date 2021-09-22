from django.conf import settings
from django.db import models
from columns.models import Column


class Task(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="task", null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    how_do_this = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="how_do")
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    pub_date = models.DateTimeField("Date of publication")
    lead_time = models.DateTimeField("Date of assignment", null=True)  # можно не заполнять
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comment', null=True)  # cascade удаленные комментарии к таску
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_text = models.CharField('Text of comment', max_length=200)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
