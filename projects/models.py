from django.db import models

# Create your models here.
class Project(models.Model):
    weight = models.IntegerField()
    classification = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)