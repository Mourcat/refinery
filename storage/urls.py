from django.urls import path

from . import views

app_name = 'storage'

urlpatterns = [
    path('storage/', views.storage_view, name='storage'),
]