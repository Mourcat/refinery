from django.shortcuts import render, get_object_or_404

from .models import Category, Equipment


def index(request):
    categories = Category.objects.all().order_by('title')
    equipment = Equipment.objects.all()
    return render(request, 'equipment/equipment.html', {'categories': categories, 'equipment': equipment})

def equipment_detail(request, slug):
    equipment = get_object_or_404(Equipment, slug=slug)
    return render(request, 'equipment/equipment_detail.html', {'equipment': equipment})