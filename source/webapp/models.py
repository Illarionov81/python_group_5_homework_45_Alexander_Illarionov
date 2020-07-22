from django.db import models

class To_Do_list(models.Model):
    description = models.TextField(max_length=3500, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=300, null=False, blank=False, default='new', verbose_name='Статус')
    completion_time = models.DateField(auto_now=False, null=True, blank=True, default=None, verbose_name='Время выполнения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.description)