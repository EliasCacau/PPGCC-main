from django.db import models



class Arquivo(models.Model):

    url = models.FileField(upload_to='media/uploads/')
    nome = models.TextField(max_length=100)
    extensao = models.TextField(max_length=10)
    data = models.DateField(auto_now_add=True)
