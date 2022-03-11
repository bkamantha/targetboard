from rest_framework import serializers
from .models import Downtime, ModuleTarget, LeanBand

# show data in api endpoint


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleTarget
        fields = '__all__'


class LeanBandSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeanBand
        fields = '__all__'


class DowntimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downtime
        fields = '__all__'
