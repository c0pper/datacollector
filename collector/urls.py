from django.urls import path
from . import views

urlpatterns = [
    path('', views.submission_form, name='submission_form'),
    path('submission_list', views.submission_list, name='submission_list'),
]
