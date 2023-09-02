from rest_framework import serializers
from .models import Calculo



class CalculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculo
        fields = '__all__'
