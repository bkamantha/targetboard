from django.urls import path, re_path
from django.conf.urls import include
from .import views
from rest_framework import routers
from targetboard.views import DowntimeViewSet, targetBoardViewSet

router = routers.DefaultRouter()
router.register('ModuleTarget', views.targetBoardViewSet)

Guest_Downtime_list = DowntimeViewSet.as_view({'get': 'list'})
Guest_TargetBoard_list = targetBoardViewSet.as_view({'get': 'list'})
Guest_Downtime_detail = DowntimeViewSet.as_view({'get': 'retrieve'})
Guest_TargetBoard_detail = targetBoardViewSet.as_view({'get': 'retrieve'})

Downtime_list = DowntimeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

TargetBoard_list = targetBoardViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

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

urlpatterns = [
    # Guest Mode
    path('Guest/Downtime/', Guest_Downtime_list, name='Guest_Downtime_list'),
    path('Guest/TargetBoard/', Guest_TargetBoard_list),
    path('Guest/Downtime/<int:pk>/', Guest_Downtime_detail,
         name='Guest_Downtime_detail'),
    path('Guest/TargetBoard/<int:pk>/',
         Guest_TargetBoard_detail, name='Guest_TargetBoard_detail'),

    # Admin Mode
    path('Downtime/', Downtime_list, name='Downtime_list'),
    path('TargetBoard/', TargetBoard_list, name='TargetBoard_detail'),
    path('Downtime/<int:pk>/', Downtime_detail, name='Downtime_detail'),
    path('TargetBoard/<int:pk>/', TargetBoard_detail, name='TargetBoard_detail'),
    path('', include(router.urls)),
]
