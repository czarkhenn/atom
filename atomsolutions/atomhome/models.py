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
    
    class Meta:
        verbose_name = 'Post (ENG)'
        verbose_name_plural = 'Posts (ENG)'

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

class Postjp(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='持ち主')
    title = models.CharField(max_length=255, verbose_name='表題')
    content = models.TextField(max_length=500, verbose_name='内容')
    created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='作成した')
    modified = models.DateField(auto_now=True, verbose_name='修正済み')
    
    class Meta:
        verbose_name = 'Post (JP)'
        verbose_name_plural = 'Posts (JP)'

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