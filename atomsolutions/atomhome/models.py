from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date, time, timedelta
import datetime
# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.owner.username

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_label(self):
        
        if self.modified > datetime.date.today() - datetime.timedelta(days=7):
           return "NEW!" 
        else:
           return " "
