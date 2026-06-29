# from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({
        "status": "success",
        "message": "LifeLink AI Backend Running",
        "version": "0.0.1"
    })
