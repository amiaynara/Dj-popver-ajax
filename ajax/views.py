from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def PopoverView(request):
    return render(request, 'ajax/home.html')

def DataView(request):
    context={
            "name": "abhay",
            "last_name": "narayan",
            }
    return JsonResponse(context)
