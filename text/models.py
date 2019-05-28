from django.db import models
from django.utils import timezone
from django.urls import reverse

class TextPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=200)
    lang =  models.CharField(max_length=200)
    keyword = models.TextField()
    relevance = models.TextField()
    category_ibm = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title + " " + self.author.username +" "+self.created.strftime("%Y-%m-%d%H:%M:%S")

    def get_absolute_url(self):
        return reverse('textResult', args=[self.pk])