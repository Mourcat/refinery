from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from equipment.views import CategoryViewSet, EquipmentViewSet
from storage.views import BearingViewSet, MechSealViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='api-categories')
router.register(r'equipment', EquipmentViewSet, basename='api-equipment')
router.register(r'bearings', BearingViewSet, basename='api-bearings')
router.register(r'mech-seals', MechSealViewSet, basename='api-mech-seals')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('equipment.urls')),
    path('', include('storage.urls')),
    path('api/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)