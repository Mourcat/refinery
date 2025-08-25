from django.shortcuts import render
from .models import Category, Equipment


def index(request):
    categories = Category.objects.all().order_by('title')
    equipment = Equipment.objects.all()
    print([c for c in categories])
    return render(request, 'equipment/equipment.html', {'categories': categories, 'equipment': equipment})