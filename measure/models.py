from django.db import models
import uuid

class Measure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(verbose_name='codigo', max_length=20,default='20181400')
    longitud = models.IntegerField(verbose_name='longitud',default=1)
    latitud = models.IntegerField(verbose_name='latitud',default=1)
    terreno = models.CharField(verbose_name='terreno',max_length=20,default='Planicie')
    area = models.IntegerField(verbose_name='area',default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)