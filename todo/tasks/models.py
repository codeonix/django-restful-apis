from django.db import models


# Create your models here.
class TaskModel(models.Model):
    contact = models.TextField()


class SchemeModel(models.Model):
    scheme_name: models.CharField(max_length=20)