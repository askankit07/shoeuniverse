
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *

class MenViewSet(viewsets.ModelViewSet):
    queryset = MenModel.objects.all()
    serializer_class = MenModelSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            if isinstance(data, list):
                serializer = self.get_serializer(data=data, many=True)
            else:
                serializer = self.get_serializer(data=data)
            
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class WomenViewSet(viewsets.ModelViewSet):
    queryset = WomenModel.objects.all()
    serializer_class = WomenModelSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            if isinstance(data, list):
                serializer = self.get_serializer(data=data, many=True)
            else:
                serializer = self.get_serializer(data=data)
            
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class KidsViewSet(viewsets.ModelViewSet):
    queryset = KidsModel.objects.all()
    serializer_class = KidsModelSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            if isinstance(data, list):
                serializer = self.get_serializer(data=data, many=True)
            else:
                serializer = self.get_serializer(data=data)
            
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NewArrivalModelViewSet(viewsets.ModelViewSet):
    queryset = NewArrivalModel.objects.all()
    serializer_class = NewArrivalModelSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            if isinstance(data, list):
                serializer = self.get_serializer(data=data, many=True)
            else:
                serializer = self.get_serializer(data=data)
            
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

