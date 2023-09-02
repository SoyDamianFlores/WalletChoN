
from django.contrib import admin
from django.urls import include, path
from billetera import views

urlpatterns = [
    path('', views.home_view),
    path('login/', views.loginPage),
    path('register/', views.registerPage),
    path('logout/', views.logoutPage),
    path('billetera/', views.billetera_view),
    path('admin/', admin.site.urls),
    path('api/', views.api_home),
    path('api/create/', views.CalculoCreate.as_view()),
    path('api/list/', views.CalculoList.as_view()),
]
