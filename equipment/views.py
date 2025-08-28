from django.shortcuts import render, get_object_or_404

from .models import Category, Equipment


def index(request):
    categories = Category.objects.all()
    equipment = Equipment.objects.all()
    return render(request, 'equipment/equipment.html', {'categories': categories, 'equipment': equipment})

def equipment_detail(request, slug):
    categories = Category.objects.all().order_by('title')
    equipment = get_object_or_404(Equipment, slug=slug)
    return render(request, 'equipment/equipment_detail.html', {'equipment': equipment, 'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    equipment = Equipment.objects.all().filter(category=category_id).order_by('position')
    return render(request, 'equipment/category_detail.html', {'category': category, 'equipment': equipment})
