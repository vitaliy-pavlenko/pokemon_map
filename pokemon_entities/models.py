from django.db import models


class Pokemon(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', default='', blank=True)
    title_en = models.CharField(verbose_name='Название EN', max_length=200, default='', blank=True)
    title_jp = models.CharField(verbose_name='Название JP', max_length=200, default='', blank=True)
    previous_evolution = models.ForeignKey('self',
                                           on_delete=models.SET_NULL,
                                           verbose_name='Эволюция',
                                           null=True,
                                           blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта',)
    lon = models.FloatField(verbose_name='Долгота',)
    appeared_at = models.DateTimeField(verbose_name='Появился в', null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name='Исчезнет в', null=True, blank=True)
    level = models.IntegerField(verbose_name='Уровень', null=True, blank=True)
    health = models.IntegerField(verbose_name='Здоровье', null=True, blank=True)
    strength = models.IntegerField(verbose_name='Сила', null=True, blank=True)
    defence = models.IntegerField(verbose_name='Защита', null=True, blank=True)
    stamina = models.IntegerField(verbose_name='Стамина', null=True, blank=True)
