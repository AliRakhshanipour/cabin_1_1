from rest_framework.serializers import ModelSerializer
from .models import *


class TestSerializer(ModelSerializer):
    class Meta:
        model = Ride
        fields = ["id"]
