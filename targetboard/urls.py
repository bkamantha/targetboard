from django.urls import path, re_path
from django.conf.urls import include
from .import views
from rest_framework import routers
from targetboard.views import HeadViewSet, DowntimeViewSet, targetBoardViewSet, LeanBandViewSet

router = routers.DefaultRouter()
router.register('ModuleTarget', views.targetBoardViewSet)

Downtime_list = DowntimeViewSet.as_view({'get': 'list', 'post': 'create'})

TargetBoard_list = targetBoardViewSet.as_view(
    {'get': 'list', 'post': 'create'})

Head_list = HeadViewSet.as_view(
    {'get': 'list', 'post': 'create'})

Downtime_detail = DowntimeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

TargetBoard_detail = targetBoardViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

Leanband = LeanBandViewSet.as_view(
    {'get': 'list', 'post': 'create'})


urlpatterns = [
    # Admin Mode
    path('LeanBand/', Leanband, name='Leanband'),
    path('Downtime/', Downtime_list, name='Downtime_list'),
    path('Heads/', Head_list, name='Head_list'),
    path('TargetBoard/', TargetBoard_list, name='TargetBoard_detail'),
    path('Downtime/<int:pk>/', Downtime_detail, name='Downtime_detail'),
    path('TargetBoard/<int:pk>/', TargetBoard_detail, name='TargetBoard_detail'),
    path('', include(router.urls)),
]
