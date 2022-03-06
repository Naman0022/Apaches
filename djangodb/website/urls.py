
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "index"),
    path('registration_community',views.registration_community, name = "registration_community"),
    
]
