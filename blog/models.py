from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32,default='Title');
    content = models.TextField(null=True)
    #pub_time = models.DateTimeField(auto_now=True)
    pub_time = models.DateTimeField(null=True)

    def __str__(self):
        #以title作为实例化后的名称
        return self.title