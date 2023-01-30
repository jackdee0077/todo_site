from django.db import models

# Create your models here.

class Tag(models.Model):
    name= models.CharField(max_length=30)

class Task(models.Model):
    '''A task object will have a description of the task to complete'''
    description = models.CharField(max_length=255)
    tags= models.ManyToManyField(Tag)

class Comment(models.Model):
    '''id will be set for us'''
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

