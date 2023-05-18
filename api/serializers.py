
from rest_framework import serializers
from .models import Job, Step
from rest_framework.serializers import ModelSerializer
#from .models import Job

"""
class JobSerializer(ModelSerializer):
    class Meta:

        model = Job
        fields = '__all__'
"""

class StepSerializer(serializers.ModelSerializer):
    #job = JobSerializer()
    #job_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Job.objects.all())

    class Meta:
        model = Step
        #fields = '__all__'
        fields = ('job_id','step_code','status','end_time')
   

"""
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'karma')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'owner')
        

class PostSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer(read_only=True)
    ownerId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=UserProfile.objects.all(), source='owner')
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'owner', 'ownerId', 'comments')

  
                   

class ImagenSerializer(serializers.ModelSerializer):
    job = JobSerializer()
    imagenes = serializers.ListField(
        child=serializers.ImageField(), required=False)

    class Meta:
        model = Images
        fields = ['job','imagenes']"""
