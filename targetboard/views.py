from django.http import HttpResponse, JsonResponse
from rest_framework import filters, generics, viewsets
from .serializers import HeadsconfigSerializer, ModuleSerializer, LeanBandSerializer, HeadSerializer, DowntimeSerializer
from .models import HeadDowntime, HeadsTarget, LeanBand, ModuleTarget, DowntimeCode
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class targetBoardViewSet(viewsets.ModelViewSet):
    queryset = ModuleTarget.objects.all()
    serializer_class = ModuleSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['TDate']

    # def list(self, request):
    #     return HttpResponse({"Connected to dashboard"}, status=200)

    def create(self, request):
        TDate = request.data['TDate']
        Shift = request.data['Shift']
        HeadCount = request.data['HeadCount']
        lb_Id = request.data['lb_Id']
        bandID = LeanBand.objects.get(pk=lb_Id)

        record = ModuleTarget.objects.create(lb_Id=bandID,
                                             TDate=TDate, Shift=Shift, HeadCount=HeadCount)

        return JsonResponse({"recordID": record.pk, "Heads": int(HeadCount)}, status=200)


class HeadConfigViewSet(viewsets.ModelViewSet):
    queryset = HeadsTarget.objects.all()
    serializer_class = HeadsconfigSerializer


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
