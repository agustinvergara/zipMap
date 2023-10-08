from django.urls import path
from . import views

app_name = 'zip_info'

urlpatterns = [
    path('postal_code/', views.zipcode_capture, name='postal_code_capture'),
]
