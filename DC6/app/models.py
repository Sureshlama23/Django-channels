from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=250,unique=True)
    def __str__(self):
        return self.name
    
class Chat(models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='chating_group_name')
    