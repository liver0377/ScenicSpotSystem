from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Province


# Create your views here.


from django.shortcuts import render
from .models import Province

def home(request):
    try:
        province = Province.objects.first()
        scenic_spots = []

        if province:
            scenic_spots = province.scenic_spots.all()

        return render(request, "scenic_spots.html", {
            "provinces": Province.objects.all(),
            "scenic_spots": scenic_spots,
            "cur_province": province
        })

    except Exception as e:
        return render(request, "error.html", {"error_message": str(e)})



def province_spots(request, province_name):
    try:
        province = get_object_or_404(Province, name=province_name)
        scenic_spots = province.scenic_spots.all()

        return render(request, "scenic_spots.html", {
            "provinces": Province.objects.all(),
            "scenic_spots": scenic_spots,
            "cur_province": province
        })
    
    except Http404:
        return render(request, "error.html", {"error_message": "Province not found."})

