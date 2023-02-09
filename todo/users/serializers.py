import math

from rest_framework import serializers
from .models import SchemeData


class SchemeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemeData
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        for key, value in representation.items():
            if isinstance(value, float) and math.isnan(value):
                representation[key] = None
        return representation
