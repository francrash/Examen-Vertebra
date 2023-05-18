from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import serializers
# Create your views here.

from .models import Job, Images
from .serializers import JobSerializer, ImagenSerializer


@api_view(['POST'])
def post_image(request):
    data = request.data
    images = Images.objects.create(

    )
