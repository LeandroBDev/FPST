from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.main_interno, name='main_interno'),
]