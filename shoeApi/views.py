from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *

class BaseProductModelViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet that handles the common create method logic.
    """
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            many = isinstance(data, list)
            serializer = self.get_serializer(data=data, many=many)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Concrete ViewSets inheriting from the base class
class MenViewSet(BaseProductModelViewSet):
    queryset = MenModel.objects.all()
    serializer_class = MenModelSerializer

class WomenViewSet(BaseProductModelViewSet):
    queryset = WomenModel.objects.all()
    serializer_class = WomenModelSerializer

class KidsViewSet(BaseProductModelViewSet):
    queryset = KidsModel.objects.all()
    serializer_class = KidsModelSerializer

class NewArrivalModelViewSet(BaseProductModelViewSet):
    queryset = NewArrivalModel.objects.all()
    serializer_class = NewArrivalModelSerializer
