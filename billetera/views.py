from django.shortcuts import redirect, render
from .forms import BilleteraForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.generics import CreateAPIView
from .models import Calculo
from .serializers import CalculoSerializer  
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Calculo
from .serializers import CalculoSerializer
from django.http import JsonResponse


class CalculoCreate(CreateAPIView):
    queryset = Calculo.objects.all()
    serializer_class = CalculoSerializer

class CalculoList(ListAPIView):
    queryset = Calculo.objects.all()
    serializer_class = CalculoSerializer

def api_home(request):
    message = "Bienvenido a la API de cálculos. Consulta la documentación para obtener más información sobre cómo usar la API."
    return JsonResponse({"message": message})




def calcular_porcentajes(ingresos_mensuales, gasto_alquiler, gasto_comida, gasto_transporte, gasto_telefonia, gasto_gimnasio, gasto_fiestas, gasto_restaurant, gasto_shopping, gasto_otros):
    
    # Calcula los porcentajes de los gastos fijos en relación con los ingresos mensuales
        porcentaje_alquiler = (gasto_alquiler / ingresos_mensuales) * 100
        porcentaje_comida = (gasto_comida / ingresos_mensuales) * 100
        porcentaje_transporte = (gasto_transporte / ingresos_mensuales) * 100
        porcentaje_telefonia = (gasto_telefonia / ingresos_mensuales) * 100
        porcentaje_gimnasio = (gasto_gimnasio / ingresos_mensuales) * 100

    # Calcula los porcentajes de los gastos eventuales en relación con los ingresos mensuales
        porcentaje_fiestas = (gasto_fiestas / ingresos_mensuales) * 100
        porcentaje_restaurant = (gasto_restaurant / ingresos_mensuales) * 100
        porcentaje_shopping = (gasto_shopping / ingresos_mensuales) * 100
        porcentaje_otros = (gasto_otros / ingresos_mensuales) * 100
        

        return {
            'porcentaje_alquiler': porcentaje_alquiler,
            'porcentaje_comida': porcentaje_comida,
            'porcentaje_transporte': porcentaje_transporte,
            'porcentaje_telefonia': porcentaje_telefonia,
            'porcentaje_gimnasio': porcentaje_gimnasio,
            'porcentaje_fiestas': porcentaje_fiestas,
            'porcentaje_restaurant': porcentaje_restaurant,
            'porcentaje_shopping': porcentaje_shopping,
            'porcentaje_otros': porcentaje_otros,
            # Agrega más porcentajes según sea necesario
        }




def billetera_view(request):
    if request.method == 'POST':
        form = BilleteraForm(request.POST)
        if form.is_valid():
            ingresos_mensuales = form.cleaned_data['ingresos_mensuales']
            
            porcentaje_ahorro = form.cleaned_data['porcentaje_ahorro']

            # Obtén los valores de los gastos fijos dinámicos
            gasto_alquiler = form.cleaned_data['gasto_alquiler']
            gasto_comida = form.cleaned_data['gasto_comida']
            gasto_transporte = form.cleaned_data['gasto_transporte']
            gasto_telefonia = form.cleaned_data['gasto_telefonia']
            gasto_gimnasio = form.cleaned_data['gasto_gimnasio']

           

            # Calcula el total de los gastos fijos
            total_gastos_fijos = gasto_alquiler + gasto_comida + gasto_transporte + gasto_telefonia + gasto_gimnasio


            # Obtén los valores de los gastos eventuales dinámicos
            gasto_fiestas = form.cleaned_data['gasto_fiestas']
            gasto_restaurant = form.cleaned_data['gasto_restaurant']
            gasto_shopping = form.cleaned_data['gasto_shopping']
            gasto_otros = form.cleaned_data['gasto_otros']

       

            # Calcula el total de los gastos eventuales
            total_gastos_eventuales = gasto_fiestas + gasto_restaurant + gasto_shopping + gasto_otros

            # Calcula el ahorro actual y el ahorro deseado
            ahorro = ingresos_mensuales - total_gastos_fijos - total_gastos_eventuales
            ahorro_deseado = ingresos_mensuales * (porcentaje_ahorro / 100)

            # Determina si los ahorros van bien
            ahorros_van_bien = ahorro >= ahorro_deseado
            

            # Aquí creamos un nuevo cálculo y lo guardamos en la API
            nuevo_calculo = {
                'usuario': request.user.id,  # Suponiendo que tienes una autenticación de usuario
                'ahorro': ahorro,
                'ahorro_deseado': ahorro_deseado,
                'ahorros_van_bien': ahorros_van_bien
            }
            response = requests.post('http://localhost:8000/api/create/', data=nuevo_calculo)

            porcentajes = calcular_porcentajes(ingresos_mensuales, gasto_alquiler, gasto_comida, gasto_transporte, gasto_telefonia, gasto_gimnasio, gasto_fiestas, gasto_restaurant, gasto_shopping, gasto_otros)
            # Verificamos si la creación fue exitosa
            if response.status_code == status.HTTP_201_CREATED:
                # Redirigimos a la vista de resultados con los datos calculados
                return render(request, 'resultados.html', {
                    'ahorro': ahorro,
                    'ahorro_deseado': ahorro_deseado,
                    'ahorros_van_bien': ahorros_van_bien,
                    'gasto_alquiler': gasto_alquiler,
                    'gasto_comida': gasto_comida,
                    'gasto_transporte': gasto_transporte,
                    'gasto_telefonia': gasto_telefonia,
                    'gasto_gimnasio': gasto_gimnasio,
                    'gasto_fiestas': gasto_fiestas,
                    'gasto_restaurant': gasto_restaurant,
                    'gasto_shopping': gasto_shopping,
                    'gasto_otros': gasto_otros,
                    'porcentaje_alquiler': porcentajes['porcentaje_alquiler'],
                    'porcentaje_comida': porcentajes['porcentaje_comida'],
                    'porcentaje_transporte': porcentajes['porcentaje_transporte'],
                    'porcentaje_telefonia': porcentajes['porcentaje_telefonia'],
                    'porcentaje_gimnasio': porcentajes['porcentaje_gimnasio'],
                    'porcentaje_fiestas': porcentajes['porcentaje_fiestas'],
                    'porcentaje_restaurant': porcentajes['porcentaje_restaurant'],
                    'porcentaje_shopping': porcentajes['porcentaje_shopping'],
                    'porcentaje_otros': porcentajes['porcentaje_otros'],
                })
            else:
                messages.error(request, 'Hubo un error al guardar el cálculo.')


    else:
        form = BilleteraForm()
    return render(request, 'billetera.html', {'form': form})

   

def loginPage(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('/')
            
           
        messages.error(request, 'Incorrect Login') 

    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect('/')


def registerPage(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if (password != confirm_password):
            messages.error(request, 'Invalid Confirm Password')
            return redirect('/register')
        User.objects.create_user(username, email=email, first_name=name, last_name=lastname, password=password)
        return redirect('/login')
    return render(request, 'register.html')


def home_view(request):
    return render(request, 'home.html')




