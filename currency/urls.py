from django.urls import path
from .views import UpdateCurrency, Rate

urlpatterns = [
    path('', Rate.as_view()),
    path('update_rate/<str:symbol>/', UpdateCurrency.as_view()),

]
