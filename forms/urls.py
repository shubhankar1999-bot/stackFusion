from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',test),
    path('post_form/',add_Form),
    path('delete_data/<id>/',delete_form_data)
]