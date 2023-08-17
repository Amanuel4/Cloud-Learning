from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    image=models.ImageField(upload_to='images/')
    file = models.FileField(upload_to= 'documents/', default='null')
    author=models.CharField(max_length=30)
    title=models.CharField(max_length=60)
    content=models.TextField()
    date= models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.author+' '+ '('+ self.title +')'