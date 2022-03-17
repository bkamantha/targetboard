from django.http import HttpResponse
from rest_framework import filters, generics, viewsets
from .serializers import ModuleSerializer, LeanBandSerializer, DowntimeSerializer
from .models import ModuleTarget, LeanBand, Downtime
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class targetBoardViewSet(viewsets.ModelViewSet):
    queryset = ModuleTarget.objects.all()
    serializer_class = ModuleSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['TDate']


class DowntimeViewSet(viewsets.ModelViewSet):
    queryset = Downtime.objects.all()
    serializer_class = DowntimeSerializer


class LeanBandViewSet(viewsets.ModelViewSet):
    queryset = LeanBand.objects.all()
    serializer_class = LeanBandSerializer
