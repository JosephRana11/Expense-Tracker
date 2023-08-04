from django.urls import path
from .views import record_income_view

urlpatterns = [
    path('record-income' , record_income_view , name = 'record-income')
]
