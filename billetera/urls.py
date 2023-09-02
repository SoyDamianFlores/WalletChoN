# En billetera/urls.py
from django.urls import path, include
from .views import billetera_view
from .views import home_view
from .views import login
from .views import CalculoCreate, CalculoList
from .views import billetera_view, home_view, loginPage, registerPage, logoutPage, api_home



urlpatterns = [
    path('', home_view, name='home'),  
    path('billetera/', billetera_view, name='billetera'),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutPage, name='logout'),
    path('api/', api_home, name='api-home'),
    path('api/create/', CalculoCreate.as_view(), name='calculo-create'),
    path('api/list/', CalculoList.as_view(), name='calculo-list'),
]