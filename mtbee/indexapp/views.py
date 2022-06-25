from re import template
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Hoge, Roulette
from django.http import HttpResponse
import csv

# 発注リスト
class HogeIndex(ListView):
    model = Hoge
    context_object_name = "index"

class HogeDetail(DetailView):
    model = Hoge


class HogeCreate(CreateView):
    model = Hoge
    fields = "__all__"
    success_url = reverse_lazy("index_list")

class HogeUpdate(UpdateView):
    model = Hoge
    fields = "__all__"
    success_url = reverse_lazy("index_list")


class HogeDelete(DeleteView):
    model = Hoge
    success_url = reverse_lazy("index_list")

def Hoge_csvdownload(request):
    response = HttpResponse(content_type="text/csv; charset=cp932")
    response['Content-Disposition'] = 'attachment; filename = index.csv'
    writer = csv.writer(response)
    writer.writerow([
        "No.",
        "コード",
        "品名",
        "数量",
        "備考",
    ])
    for post in Hoge.objects.all():
        writer.writerow([
            post.number,
            post.code,
            post.name,
            post.quantity,
            post.description])
    return response

    # ルーレット
class RouletteIndex(ListView):
    queryset = Roulette.objects.order_by('?')[:20]
    context_object_name = "roulette_ex"
    template_name = "roulette_list.html"


class RouletteDelete(DeleteView):
    model = Roulette
    success_url = reverse_lazy("roulette_list")

class RouletteCreate(CreateView):
    model = Roulette
    fields = "__all__"
    success_url = reverse_lazy("roulette_list")

    
    #旅行地図
def index(request) :
    return render(request, "map/index.html")

    #トップ
def top(request) :
    return render(request, "top.html")