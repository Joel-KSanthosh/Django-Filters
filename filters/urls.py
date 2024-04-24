from django.urls import path
from .views import GenusViewset

urlpatterns = [
    path('animal/', GenusViewset.as_view({'get': 'list',})),
]