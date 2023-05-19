from rest_framework.routers import DefaultRouter
from api.views import JobViewSet


router_jobs = DefaultRouter()

router_jobs.register(prefix='step', basename='step', viewset=JobViewSet)
