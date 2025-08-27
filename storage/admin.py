from django.contrib import admin
from django.http.request import HttpRequest
from unfold.admin import ModelAdmin

from .models import Bearing, MechSeal


@admin.register(Bearing)
class BearingAdmin(ModelAdmin):
    list_display = ("manufacturer", "number", "element_type", "inner_diameter", "outer_diameter")
    list_filter = ("manufacturer", "element_type")
    search_fields = ("manufacturer", "number")
    ordering = ["manufacturer", "number"]
    
    def get_prepopulated_fields(self, request, obj = None):
        """
        Retrieves the prepopulated fields for the given request and object.
        """
        return {"slug": ("manufacturer", "number",)}


@admin.register(MechSeal)
class MechSealAdmin(ModelAdmin):
    list_display = ("manufacturer", "label","assembly_code")
    list_filter = ("manufacturer", "label")
    search_fields = ("manufacturer", "label", "assembly_code")
    ordering = ["manufacturer", "label", "assembly_code"]
    
    def get_prepopulated_fields(self, request, obj = None):
        """
        Retrieves the prepopulated fields for the given request and object.
        """
        return {"slug": ("manufacturer", "label", "assembly_code",)}