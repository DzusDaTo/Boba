from django.db import models


class Svaz(models.Model):
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    sposob = models.CharField('Способ обратной связи', max_length=100)
    create_at = models.DateTimeField('Дата', auto_now_add=True)
    pravki = models.TextField('Предложенные правки', max_length=1000)
    otvet = models.BooleanField('Ответили', default=False)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Связь с администратором'
        verbose_name_plural = 'Связь с администратором'
