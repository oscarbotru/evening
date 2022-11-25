from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Kitchen(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    country = models.CharField(max_length=100, verbose_name='Страна происхождения', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='Активно')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'кухня'
        verbose_name_plural = 'кухни'


class Receipt(models.Model):
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, verbose_name='Кухня мира')

    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    ingredients = models.TextField(verbose_name='Ингредиенты')

    is_active = models.BooleanField(default=True, verbose_name='Активно')

    def __str__(self):
        return f'{self.title} ({self.kitchen.title})'

    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

