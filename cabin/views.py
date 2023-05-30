from rest_framework.viewsets import ModelViewSet
from .queries import *
from .serializers import TestSerializer


class TestViewSet(ModelViewSet):
    queryset = query_13("mostafa", "ali")
    serializer_class = TestSerializer
