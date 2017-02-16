from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
    stores = models.ManyToManyField(
        'catalogue.Store', through='StoreProduct',
        verbose_name=_("Store"))


class Store(models.Model):
    name = models.CharField(max_length=255)
    store_admins = models.ForeignKey(User)

    def __str__(self):
        return u'%s' % self.name


class StoreProduct(models.Model):
    store = models.ForeignKey(Store)
    product = models.ForeignKey(Product)

from oscar.apps.catalogue.models import *
