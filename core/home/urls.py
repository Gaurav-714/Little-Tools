from django.urls import path
from .views import ConvertImageView

urlpatterns = [
    path('img-to-pdf/', ConvertImageView.as_view(), name='img_to_pdf'),
]
