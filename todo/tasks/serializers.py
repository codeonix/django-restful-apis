from rest_framework import serializers

from tasks.models import SchemeModel


class SchemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SchemeModel
        fields = '__all__'
