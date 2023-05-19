from django.db import models


class Job(models.Model):
    
    # title = models.CharField(max_length=255, null=True)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)


opptions = (
    ('process', 'PROCESS'),
    ('success', 'SUCCESS'),
    ('failure', 'FAILURE'),
)


class Images(models.Model):
    job_id = models.ForeignKey(
        Job, on_delete=models.PROTECT, related_name='images')
    imagen = models.ImageField(
        max_length=50, blank='', default="", upload_to='images/')


class Step(models.Model):
    job_id = models.ForeignKey(
        Job, on_delete=models.PROTECT, related_name='steps')
    step_code = models.CharField(max_length=4)
    status = models.CharField(
        max_length=10, choices=opptions, default='process')
    start_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    image = models.ForeignKey(Images, on_delete=models.PROTECT)

    def __str__(self):
        return self.step_code

"""
class Images_pr(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.PROTECT, related_name='images_pr')
    #image_id = models.IntegerField()
    image_pr = models.ImageField(
        max_length=50, blank='', default="", upload_to='imagespr/')
    step = models.ForeignKey(Step, on_delete=models.PROTECT)
    """

"""
class Log_Error(models.Model):
    job_id = models.IntegerField()
    step_id = models.IntegerField()
    message = models.CharField(max_length=500)
    time_error = models.DateTimeField(auto_now=False, auto_now_add=True)
"""
