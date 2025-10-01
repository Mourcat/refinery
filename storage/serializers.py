from rest_framework import serializers

from .models import Bearing, MechSeal


class BearingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bearing
        fields = [
            'id', 'manufacturer', 'number', 'slug', 'image',
            'element_type', 'outer_diameter', 'inner_diameter'
        ]


class MechSealSerializer(serializers.ModelSerializer):
    class Meta:
        model = MechSeal
        fields = [
            'id', 'label', 'manufacturer', 'assembly_code', 'slug',
            'image', 'material_id', 'repair_kit_id'
        ]


