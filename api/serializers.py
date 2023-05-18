
from rest_framework import serializers
from .models import Job, Images, Step, Images_pr


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'


class ImagenSerializer(serializers.ModelSerializer):
    imagenes = serializers.ListField(
        child=serializers.ImageField(), required=False)

    class Meta:
        model = Images
        fields = ['imagenes']
