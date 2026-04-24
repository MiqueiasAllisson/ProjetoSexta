from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=200)
    address = models.CharField('Endereço', max_length=200)
    phone= models.CharField('Telefone', max_length=20, default='')
    email = models.EmailField('Email', max_length=254, default='')


    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        ordering =['id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
