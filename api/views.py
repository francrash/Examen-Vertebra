from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import serializers
from rest_framework.viewsets import ModelViewSet

from .models import Job,  Step
from .serializers import StepSerializer, JobSerializer


class JobViewSet(ModelViewSet):

    # b = Job(end_time=None)
    # b.save()

    queryset = Step.objects.all()
    serializer_class = StepSerializer


"""
@api_view(['POST'])
def post_image(request):
    data = request.data
    images = Images.objects.create(

    )"""
