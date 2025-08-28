from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Category, Equipment


def index(request):
    categories = Category.objects.all().order_by('parent', 'title')
    equipment_list = Equipment.objects.all().order_by('position')
    
    paginator = Paginator(equipment_list, 12)  # Show 12 equipment per page
    page_number = request.GET.get('page')
    equipment = paginator.get_page(page_number)
    
    return render(request, 'equipment/equipment.html', {
        'categories': categories, 
        'equipment': equipment
    })

def equipment_detail(request, slug):
    categories = Category.objects.all().order_by('parent', 'title')
    equipment = get_object_or_404(Equipment, slug=slug)
    return render(request, 'equipment/equipment_detail.html', {'equipment': equipment, 'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    categories = Category.objects.all().order_by('parent', 'title')
    equipment_list = Equipment.objects.filter(category=category_id).order_by('position')
    
    paginator = Paginator(equipment_list, 12)  # Show 12 equipment per page
    page_number = request.GET.get('page')
    equipment = paginator.get_page(page_number)
    
    return render(request, 'equipment/category_detail.html', {
        'categories': categories, 
        'category': category, 
        'equipment': equipment
    })
