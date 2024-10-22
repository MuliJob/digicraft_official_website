from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('services-details', views.service_detail, name='service_detail')
]