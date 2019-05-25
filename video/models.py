from django.db import models
from django.utils import timezone

class VideoPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    content = models.TextField()
    category = models.CharField(max_length=200)
    lang =  models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title + " " + self.author.username +" "+self.created.strftime("%Y-%m-%d%H:%M:%S")