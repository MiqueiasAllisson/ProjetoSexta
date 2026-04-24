from django.db import models

# Create your models here.class Product(models.Model): 
class SocialNetwork(models.Model):
    name = models.CharField('Nome', max_length=100)
    content_type = models.TextField('Conteúdo', max_length=200)
    url = models.CharField('URL', max_length=200) 


    class Meta:
        verbose_name = 'SocialNetwork'
        verbose_name_plural = 'SocialNetworks'
        ordering =['id']

    def __str__(self):
        return f'{self.name}'