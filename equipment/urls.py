from django.urls import path
from . import views

app_name = 'equipment'

urlpatterns = [
    path('', views.index, name='equipment'),
    path("equipment/<slug:slug>/", views.equipment_detail, name='equipment-detail'),
    #path('category/<int:category_id>', views.category_detail, name='category_detail'),
]