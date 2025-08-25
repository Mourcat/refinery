from django.shortcuts import render
from .models import Bearing, MechSeal


def storage_view(request):
    
    return render(request, 'storage/storage_view.html', )