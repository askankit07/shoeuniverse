from rest_framework import serializers
from .models import MenApi,WomenApi,KidsApi,NewArrivalApi

class MenApiSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=20,required=True)
    price=serializers.CharField(max_length=10,required=True)
    description=serializers.CharField(max_length=150,required=True)
    image=serializers.CharField(max_length=400,required=True)

    class Meta:
        model=MenApi
        fields=('__all__')

class WomenApiSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=20,required=True)
    price=serializers.CharField(max_length=10,required=True)
    description=serializers.CharField(max_length=150,required=True)
    image=serializers.CharField(max_length=400,required=True)

    class Meta:
        model=WomenApi
        fields=('__all__')

class KidsApiSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=20,required=True)
    price=serializers.CharField(max_length=10,required=True)
    description=serializers.CharField(max_length=150,required=True)
    image=serializers.CharField(max_length=400,required=True)

    class Meta:
        model=KidsApi
        fields=('__all__')

class NewArrivalSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=20,required=True)
    price=serializers.CharField(max_length=10,required=True)
    description=serializers.CharField(max_length=150,required=True)
    image=serializers.CharField(max_length=400,required=True)

    class Meta:
        model=NewArrivalApi
        fields=('__all__')