from unicodedata import name
from django.db import models

# Create your models here.

class Hoge(models.Model):
    number = models.IntegerField("No.", unique=True)
    code = models.CharField("コード", max_length=100, blank=True, null=True)
    name = models.CharField("品名", max_length=100, blank=True, null=True)
    quantity = models.IntegerField("数量", blank=True, null=True)
    description = models.TextField("備考", blank=True, null=True)

    def __str__(self):
        return self.name


class Roulette(models.Model):
    name = models.CharField("なにする？", max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name