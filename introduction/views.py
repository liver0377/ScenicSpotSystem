from django.shortcuts import render, redirect
from .models import Province

# Create your views here.

def home(request):
    province = Province.objects.first()
    scenic_spots = province.scenic_spots.all()
    return render(request, "scenic_spots.html", {"provinces": Province.objects.all(), "scenic_spots": scenic_spots, "cur_province": province})


def province_spots(request, province_name):
    province = Province.objects.get(name=province_name)
    scenic_spots = province.scenic_spots.all()
    return render(request, "scenic_spots.html", {"provinces": Province.objects.all(), "scenic_spots": scenic_spots, "cur_province": province})

