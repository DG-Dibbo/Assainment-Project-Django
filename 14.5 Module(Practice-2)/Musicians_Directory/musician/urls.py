from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_form, name='musician_form'),
    path('musician_view/<int:id>/', views.musician_detail_view, name='musician_detail_view'),
]
