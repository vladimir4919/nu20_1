from django.db import models


# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=32, verbose_name='К какой категории относится проблема')



    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='Уточненная информация о том,в какой части системы проблема')
    description = models.TextField(blank=True, verbose_name='Более подробное сообщение о проблеме')
    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=16, verbose_name='Сообщение о возникшей проблеме')
    description = models.TextField(blank=True, verbose_name='Краткое изложение проблемы')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Время регистрации сообщения')
    update = models.DateTimeField(auto_now=True, verbose_name='Время окончания работ по устранению')
    # Связь с категорией
    # один - много
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Связь с тегом
    tags = models.ManyToManyField(Tag)
