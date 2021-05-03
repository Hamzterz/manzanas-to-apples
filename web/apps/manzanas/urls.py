from django.urls import path

from web.apps.manzanas import views

urlpatterns = [
    path('', views.home, name='home'),
]