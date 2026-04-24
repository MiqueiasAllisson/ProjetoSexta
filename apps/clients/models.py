from django.db import models

# Create your models here.
from person.models import Person

# Após o comentario "# Create your models here." e crie a classe "Client" do modelo.

class Client(Person):
    gender = models.CharField('Genero', max_length=1, choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ])
    socialnetwork = models.ManyToManyField('socialnetwork.Socialnetwork', verbose_name="Redes Socias")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return super().__str__()