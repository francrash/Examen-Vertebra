
from rest_framework import serializers
from .models import Job, Step, Images
from rest_framework.serializers import ModelSerializer
# from .models import Job


class JobSerializer(ModelSerializer):

    class Meta:
        model = Job
        exclude = ('start_time', 'end_time')


class ImagenSerializer(serializers.ModelSerializer):
    job_id = JobSerializer()
    imagen = serializers.ListField(
        child=serializers.ImageField(), required=False)

    class Meta:
        model = Images
        fields = ('imagen', 'job_id')


class StepSerializer(serializers.ModelSerializer):

    # serializer_class = JobSerializer
    queryset = Job.objects.values("id")
    tuple = queryset.values_list('id', flat=True)
    lista = list(tuple)
    job_id = lista[-1]
    
    step_code = serializers.ListField(
        child=serializers.CharField(), required=False)

    class Meta:
        model = Step
        # fields = '__all__'
        fields = ['step_code', 'status', 'start_time', 'end_time']

    # def create(self, validated_data, job_id):
        """
        Create and return a new `step` instance, given the validated data.
        """
        # print(job_id)
        # return Step.objects.create(job_id=job_id**validated_data)
        # return Step.objects.create(**validated_data)


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
    ownerId = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=UserProfile.objects.all(), source='owner')
    comments = CommentSerializer(
        many=True, read_only=True, source='comment_set')

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
