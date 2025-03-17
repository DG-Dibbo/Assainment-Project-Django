from django.urls import path
from .import views
urlpatterns = [
    path('',views.forms_page,name = 'forms_page'),
    path('model/',views.home,name = 'home')
]
