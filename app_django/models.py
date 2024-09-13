from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.TextField(max_length=255)
    idade_usuario = models.IntegerField()
