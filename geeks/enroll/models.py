from django.db import models

class Student(models.Model):
    st_id = models.IntegerField()
    st_name = models.CharField(max_length=70)
    st_l_name= models.CharField(max_length=70)
    created_at = models.DateTimeField()
# Create your models here.

# will create a new model 

# will add another line of code here

# hi i am master

# hi i am feature 

# demo 