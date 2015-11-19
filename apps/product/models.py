# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Count
from django.db import connection


class CustomCategoryManager(models.Manager):
    def get_queryset(self):
        return super(CustomCategoryManager, self).get_queryset().filter(product__price__gte=100). \
            annotate(count=Count('product'))


class Category(models.Model):
    name = models.CharField(u'Категория товара', max_length=64)

    custom_objects = CustomCategoryManager()

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'Категория')
    name = models.CharField(u'Наименование товара', max_length=128)
    price = models.DecimalField(u'Цена единицы, руб.', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'

    def __unicode__(self):
        return self.name


class PhoneBuyManager(models.Manager):
    def get_buy_items(self):
        cursor = connection.cursor()
        sql = """
        SELECT phone, COUNT(user_id) FROM product_phone
        JOIN product_item
        ON product_phone.user = product_item.user_id
        WHERE product_item.status = 1
        GROUP BY phone
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def get_all_count_items(self):
        cursor = connection.cursor()
        sql = """
        SELECT T1.phone, T1.cnt1, T2.cnt1
            FROM
                (SELECT phone, COUNT(user_id) AS cnt1
                FROM product_phone
                JOIN product_item
                ON product_phone.user = product_item.user_id
                WHERE product_item.status = 1
                GROUP BY phone
               ) T1,
                (SELECT phone, COUNT(user_id) AS cnt1
                FROM product_phone
                JOIN product_item
                ON product_phone.user = product_item.user_id
                WHERE product_item.status = 0
                GROUP BY phone
              ) T2
            WHERE T2.phone = T1.phone
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


class Phone(models.Model):
    phone = models.CharField(u'Телефон', max_length=128)
    user = models.IntegerField(u'User ID')

    objects = PhoneBuyManager()

    class Meta:
        verbose_name = u'Телефон'
        verbose_name_plural = u'Телефоны'

    def __unicode__(self):
        return self.phone


STATUS = (
        (0, u'Не продано'),
        (1, u'Продано',)
)


class Item(models.Model):
    user_id = models.IntegerField(u'User ID')
    status = models.SmallIntegerField(u'Статус', choices=STATUS)

    class Meta:
        verbose_name = u'Вещь'
        verbose_name_plural = u'Вещи'

    def __unicode__(self):
        return self.get_status_display()