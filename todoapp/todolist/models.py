from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField('название задания', max_length=500)
    is_complete = models.BooleanField('завершено', default=False)


    class Meta:
        verbose_name = 'задание'
        verbose_name_plural = 'задания'


    def __str__(self):
        return self.title