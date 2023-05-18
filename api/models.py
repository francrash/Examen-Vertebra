from django.db import models


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=True)


class Images(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.PROTECT)
    imagen = models.ImageField(
        max_length=50, blank='', default="", upload_to='images/')


class Step(models.Model):

    job_id = models.ForeignKey(Job, on_delete=models.PROTECT)
    step_code = models.CharField(max_length=4)
    status = models.CharField(max_length=10)
    start_time = models.TimeField(auto_now=False, auto_now_add=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=True)
    imagen_id = models.ForeignKey(Images, on_delete=models.PROTECT)


class Images_pr(models.Model):
    image_id = models.IntegerField()
    image_pr = models.ImageField(
        max_length=50, blank='', default="", upload_to='imagespr/')
    job_id = models.IntegerField()


class Log_Error(models.Model):
    job_id = models.IntegerField()
    step_id = models.IntegerField()
    message = models.CharField(max_length=500)
    time_error = models.TimeField(auto_now=False, auto_now_add=True)
