from django.db import models

class Student(models.Model):
    st_id = models.IntegerField()
    st_name = models.CharField(max_length=70)
    st_l_name= models.CharField(max_length=70)
    created_at = models.DateTimeField()
# Create your models here.
