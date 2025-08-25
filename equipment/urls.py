from django.urls import path
from . import views

app_name = 'equipment'

urlpatterns = [
    path('', views.index, name='index'),
    #path('equipment/<int:equipment_id>', views.equipment_detail, name='equipment_detail'),
    #path('category/<int:category_id>', views.category_detail, name='category_detail'),
]