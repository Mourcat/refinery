from django.contrib import admin
from django.http.request import HttpRequest
from unfold.admin import ModelAdmin

from .models import Category, Equipment


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("title", "parent", "slug")
    ordering = ("parent", "title",)
    
    def get_prepopulated_fields(self, request, obj = None):
        """
        Retrieves the prepopulated fields for the given request and object.
        """
        return {"slug": ("title",)}
    
    
@admin.register(Equipment)
class EquipmentAdmin(ModelAdmin):
    list_display = ("position", "manufacturer", "label", "inventory_number")
    list_filter = ("category",)
    search_fields = ("position", "label", "inventory_number")
    ordering = ("position", "label")

    def get_prepopulated_fields(self, request: HttpRequest, obj = None):
        """
        Retrieves the prepopulated fields for the given request and object.
        """
        return {"slug": ("position", "label",)}