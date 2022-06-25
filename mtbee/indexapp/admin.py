from django.contrib import admin

# Register your models here.
from .models import Hoge, Roulette

admin.site.register(Hoge)
admin.site.register(Roulette)