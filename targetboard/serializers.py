from rest_framework import serializers
from .models import LeanBand, ModuleTarget, HeadsTarget, DowntimeCode, HeadDowntime
# show data in api endpoint


class ModuleSerializer(serializers.ModelSerializer):  # setup 1
    class Meta:
        model = ModuleTarget
        fields = '__all__'


class HeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadsTarget
        fields = '__all__'


class HeadsconfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadsTarget
        fields = ['module_id','HeadNumber','Style','Size','planhour','potenetialhour']


class DowntimeCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DowntimeCode
        fields = '__all__'


class LeanBandSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeanBand
        fields = '__all__'


class DowntimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadDowntime
        fields = '__all__'
