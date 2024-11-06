from rest_framework import serializers
from .models import *

class BaseProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'  # Common configuration for all product serializers

# Concrete serializers inheriting from the base serializer
class MenModelSerializer(BaseProductModelSerializer):
    class Meta(BaseProductModelSerializer.Meta):
        model = MenModel

class WomenModelSerializer(BaseProductModelSerializer):
    class Meta(BaseProductModelSerializer.Meta):
        model = WomenModel

class KidsModelSerializer(BaseProductModelSerializer):
    class Meta(BaseProductModelSerializer.Meta):
        model = KidsModel

class NewArrivalModelSerializer(BaseProductModelSerializer):
    class Meta(BaseProductModelSerializer.Meta):
        model = NewArrivalModel
