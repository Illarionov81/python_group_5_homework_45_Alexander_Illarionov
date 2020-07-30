from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class To_Do_list(models.Model):
    summary = models.CharField(max_length=300, null=False, blank=False, default="None description", verbose_name='Задание')
    description = models.TextField(max_length=3500, null=True, blank=True, default="None description", verbose_name='Описание')
    status = models.CharField(max_length=300, null=False, blank=False, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    completion_time = models.DateField(null=True, blank=True, default=None, verbose_name='Время выполнения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.description)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'