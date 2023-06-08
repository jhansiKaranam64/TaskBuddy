from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.
class Task(models.Model):

    title = models.CharField(max_length=100,null=True)
    content = models.TextField(null=True, blank=True)
    data_posted = models.DateTimeField(auto_now_add=True,null=True)
    completed = models.BooleanField(default=False)
    due = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)


    user = models.ForeignKey(User,max_length=10,on_delete=models.CASCADE,null=True)

   


