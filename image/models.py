from django.db import models
from django.utils import timezone
from django.urls import reverse

class ImagePost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pdf = models.FileField(null=True)
    content = models.TextField()
    category = models.CharField(max_length=200)
    lang =  models.CharField(max_length=200)
    keyword = models.TextField()
    relevance = models.TextField()
    category_ibm = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    index = models.TextField(null=True  )
    def __str__(self):
        return self.title + " " + self.author.username +" "+self.created.strftime("%Y-%m-%d%H:%M:%S")

    def get_absolute_url(self):
        return reverse('imageResult', args=[self.pk])
