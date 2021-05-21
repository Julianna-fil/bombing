from django.db import models


# Create your models here.
class Info(models.Model):
    id = models.IntegerField(primary_key=True)
    id_old = models.IntegerField()
    num_pp = models.IntegerField('№ п/п')
    num_report = models.IntegerField('№ сводки')
    date = models.CharField('Дата', max_length=255, default='')
    district = models.CharField('Район', max_length=255, default='')
    street_and_house = models.CharField('Улица, дом', max_length=255, default='')
    object = models.CharField('Объект', max_length=255, default='')
    high_explosive_AB = models.IntegerField('ФАБ', default=0)  # ФАБ
    incendiary_AB = models.IntegerField('ЗАБ', default=0)  # ЗАБ
    projectile = models.IntegerField('Снаряд', default=0)  # снаряд
    damage = models.CharField('Нанесённый ущерб', max_length=255, default='')
    killed = models.IntegerField('Убито', default=0)
    wounded = models.IntegerField('Ранено', default=0)
    detection_time = models.CharField('Время обнаружения', max_length=255, default='')
    adress_act = models.CharField('Актуальный адрес', max_length=255, default='')
    coordinates1 = models.FloatField('Широта')
    coordinates2 = models.FloatField('Долгота')

    class Meta:
        verbose_name = "запись таблицы"
        verbose_name_plural = "Все записи таблицы"


"""
 coordinates1
coordinates2
address
Object
Время обнаружения
Ранено
Убито
Причиненный ущерб
Снаряд
ЗАБ (зажигательная Ав бомб)
ФАБ (фугасная)
Объект
Улица, дом
Район
Дата
№ сводки
№ п/п
Unnamed: 0.1
Unnamed: 0
"""
