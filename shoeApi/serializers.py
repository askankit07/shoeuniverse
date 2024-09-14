from rest_framework import serializers
from .models import *

class MenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenModel
        fields = '__all__'

class WomenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WomenModel
        fields = '__all__'

class KidsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = KidsModel
        fields = '__all__'

class NewArrivalModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewArrivalModel
        fields = '__all__'
