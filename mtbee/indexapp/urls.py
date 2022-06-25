from operator import index
from django.urls import path
from . import views
from .views import (top,
HogeIndex, HogeDetail, HogeCreate, HogeUpdate, HogeDelete, Hoge_csvdownload,
RouletteIndex, RouletteCreate, RouletteDelete, index)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.top, name="top"),


    #インデックス
    path("index/list", HogeIndex.as_view(), name="index_list"),
    path("index/create", HogeCreate.as_view(), name="index_create"),
    path("index/detail/<int:pk>", HogeDetail.as_view(), name="index_detail"),
    path("index/update/<int:pk>", HogeUpdate.as_view(), name="index_update"),
    path("index/delete/<int:pk>", HogeDelete.as_view(), name="index_delete"),
    path("index/csv/", Hoge_csvdownload, name="index_csv"),

    #ルーレット
    path("roulette/list", RouletteIndex.as_view(), name="roulette_list"),
    path("roulette/create", RouletteCreate.as_view(), name="roulette_create"),
    path("roulette/delete/<int:pk>", RouletteDelete.as_view(), name="roulette_delete"),

    #マップ
    path("map", index, name="map"),
]