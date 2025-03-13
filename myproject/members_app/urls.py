from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_view, name='input_view'),
    path('output/', views.output_view, name='output_view'),
    path('session/', views.session_view, name='session_view'),
]