from django.db import models

class articleModel(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='img/')
    body = models.TextField()
    #body_list = raw_body.split('\n')
    #body = ''.join(['<p>' + line + '</p>' for line in body_list])
    def __str__(self):
        return self.title

class loginModel(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username