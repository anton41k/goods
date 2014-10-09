# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Spacies(models.Model):
    spacies = models.CharField(max_length=50,verbose_name=u'Тип товара')
    def __unicode__(self):
        return u'%s'%(self.spacies)
    class Meta:
        verbose_name_plural = "Тип товара"
        ordering=['spacies']

class Brand(models.Model):
    brand = models.CharField(max_length=50, verbose_name=u'Марка товара')
    spacies = models.ForeignKey('Spacies',  verbose_name=u'Тип товара')
    def __unicode__(self):
        return u'%s'%(self.brand)
    class Meta:
        verbose_name_plural = "Марка товара"
        ordering=['brand']

class Goods(models.Model):
    sort = models.CharField(max_length=50, verbose_name=u'Вид товара')
    capacity = models.CharField(max_length=5, verbose_name=u'Литраж')
    amount = models.IntegerField(verbose_name=u'Общее количество')
    spacies = models.ForeignKey('Spacies', related_name='spaciess', verbose_name=u'Тип товара')
    brand = models.ForeignKey('Brand', related_name='brands', verbose_name=u'Марка товара')
    def __unicode__(self):
        return u'%s %s "%s" %s'%(self.spacies, self.brand, self.sort, self.capacity)
    class Meta:
        verbose_name_plural = "Товар"
        ordering=['spacies','brand','sort','capacity']

class Expense(models.Model):
    date = models.DateTimeField(verbose_name=u'Дата', default=timezone.now)
    expense = models.IntegerField(verbose_name=u'Расход', blank=True, null=True)
    retrieve = models.IntegerField(verbose_name=u'Возврат', blank=True, null=True)
    coming = models.IntegerField(verbose_name=u'Приход', blank=True, null=True)
    goods = models.ForeignKey('Goods', verbose_name=(u'Товар'), related_name='expense')
    def __unicode__(self):
        return u'%s'%(self.goods)
    class Meta:
        verbose_name_plural = "Расход/Возврат/Приход"
        ordering=['date']


