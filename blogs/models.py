from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='заголовок')
    content = models.TextField(blank=True, null=True, verbose_name='содержимое')
    image = models.ImageField(upload_to='blogs/images', blank=True, null=True, verbose_name='превью (изображение)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    publication = models.BooleanField(verbose_name='признак публикации', default=True)
    views = models.PositiveIntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
