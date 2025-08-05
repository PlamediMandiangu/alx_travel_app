from django.urls import path
from . import views

urlpatterns = [
    # Add your API views here; for now, just a simple example:
    path('', views.index, name='index'),
]
