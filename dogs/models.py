from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Порода')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='Кличка')
    # category = models.CharField(max_length=100, verbose_name='Парода')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Порода')
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='Фото')
    birth_day = models.DateField(**NULLABLE, verbose_name='Дата рождения')
    objects = models.Manager()

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    class Meta:
        verbose_name = 'собаки'
        verbose_name_plural = 'собаки'

