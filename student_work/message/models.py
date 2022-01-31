from datetime import datetime
from django.db import models

class Message(models.Model):
    user = models.CharField(max_length=512,blank=False,null = False)
    text =models.TextField(max_length=2048,blank=False,null = False)
    

    def __str__(self):
        return self.user