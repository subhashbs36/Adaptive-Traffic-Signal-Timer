from django.urls import path
from . import views


urlpatterns = [
    path('process_image/', views.process_images, name='process_images'),
    path('lane_data_view/', views.lane_data_view, name='lane_data_view'),
]
