from django.shortcuts import render
from .models import Bearing, MechSeal
from rest_framework import viewsets, permissions
from .serializers import BearingSerializer, MechSealSerializer


def storage_view(request):
    
    return render(request, 'storage/storage_view.html', )


class BearingViewSet(viewsets.ModelViewSet):
    queryset = Bearing.objects.all().order_by('manufacturer', 'number')
    serializer_class = BearingSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class MechSealViewSet(viewsets.ModelViewSet):
    queryset = MechSeal.objects.all().order_by('manufacturer', 'label', 'assembly_code')
    serializer_class = MechSealSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]