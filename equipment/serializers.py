from rest_framework import serializers

from .models import Category, Equipment
from storage.models import Bearing, MechSeal


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'title', 'parent', 'description', 'slug', 'image'
        ]


class EquipmentSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    mech_seal = serializers.PrimaryKeyRelatedField(queryset=MechSeal.objects.all(), allow_null=True, required=False)
    bearings = serializers.PrimaryKeyRelatedField(queryset=Bearing.objects.all(), many=True, required=False)

    class Meta:
        model = Equipment
        fields = [
            'id', 'category', 'position', 'manufacturer', 'label',
            'inventory_number', 'slug', 'description', 'image',
            'mech_seal', 'bearings'
        ]


