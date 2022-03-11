from django.urls import path
from django.conf.urls import include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ModuleTarget', views.targetBoardViewSet)
router.register('Downtime', views.DowntimeViewSet)
router.register('LeanBand', views.LeanBandViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
