from django.urls import path
from billetera.views import CalculoCreate, CalculoList

urlpatterns = [
    path('api/create/', CalculoCreate.as_view(), name='calculo-create'),
    path('api/list/', CalculoList.as_view(), name='calculo-list'),
   
]