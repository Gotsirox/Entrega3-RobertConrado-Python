from django.db import models
from datetime import datetime
# Create your models here.

class cliente(models.Model):
    names = models.CharField(max_length=30)
    surnames = models.CharField(max_length=30)
    client_id = models.IntegerField()
    dat_ini = models.DateField()
    salary = models.IntegerField()

    def __str__(self):
        return f'Nombres: {self.names} Apellidos: {self.surnames} Id: {self.client_id} Fecha Vinculo: {self.dat_ini} Salario: {self.salary}'