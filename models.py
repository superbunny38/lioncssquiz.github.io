from django.db import models

class Message(models.Model):
    words = models.CharField(max_length=100, blank=True)
    writer = models.CharField(max_length=20, blank=True)
    date = models.DateField()
    
