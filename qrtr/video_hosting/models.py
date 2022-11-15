from django.core.validators import FileExtensionValidator
from django.db import models


class Ip(models.Model): # наша таблица где будут айпи адреса
    ip = models.CharField('IP-адрес', max_length=100)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'IP'
        verbose_name_plural = 'IP'


class Video(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.TextField('Анонс статьи')
    image = models.ImageField('Фотография', upload_to='image/')
    file = models.FileField('Видео',
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    create_at = models.DateTimeField('Дата', auto_now_add=True)
    is_published = models. BooleanField('Публикация', default=False)
    views = models.ManyToManyField(Ip, related_name="post_views", blank=True, verbose_name=('IP-адрес'))

    def __str__(self):
        return self.title

    def total_views(self):
        return self.views.count()

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
