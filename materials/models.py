from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image_preview = models.ImageField(verbose_name='превью-картинка', upload_to='image/', **NULLABLE)

    price = models.PositiveIntegerField(default=4000, verbose_name='цена за курс')
    price_id = models.CharField(max_length=100, **NULLABLE)
    product_id = models.CharField(max_length=100, **NULLABLE)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('title',)

    def __str__(self):
        return f'{self.title} - {self.description[:20]}'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='Описание')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson', verbose_name='курс')
    image = models.ImageField(upload_to='product_image/', verbose_name='Изображение', **NULLABLE)
    url_video = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.title} - {self.description[:20]}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('title',)
