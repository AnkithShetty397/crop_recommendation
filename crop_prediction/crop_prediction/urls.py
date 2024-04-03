from django.urls import path
from crop_prediction.views import predict_view

urlpatterns = [
    path('predict/', predict_view, name='predict'),
]
