from django.http import HttpResponse
from rest_framework import filters, generics, viewsets
from .serializers import ModuleSerializer, LeanBandSerializer, HeadSerializer, DowntimeSerializer
from .models import HeadDowntime, HeadsTarget, LeanBand, ModuleTarget, DowntimeCode
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class targetBoardViewSet(viewsets.ModelViewSet):
    queryset = ModuleTarget.objects.all()
    serializer_class = ModuleSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['TDate']


class HeadViewSet(viewsets.ModelViewSet):
    queryset = HeadsTarget.objects.all()
    serializer_class = HeadSerializer


class DowntimeViewSet(viewsets.ModelViewSet):
    queryset = HeadDowntime.objects.all()
    serializer_class = DowntimeSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['DTDate']


class LeanBandViewSet(viewsets.ModelViewSet):
    queryset = LeanBand.objects.all()
    serializer_class = LeanBandSerializer
