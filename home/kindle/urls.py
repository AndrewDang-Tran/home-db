from django.urls import path, include
from . import views


urlpatterns = [
    path(r'v1/kindle', views.KindleView.as_view(), name='kindle'),
]
