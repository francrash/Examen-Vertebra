# Generated by Django 4.2.1 on 2023-05-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
