from django.db import models


class Phone(models.Model):

    """
    Класс для описания модели телефонов
    """

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image')
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __repr__(self) -> str:
        return f'(id: {self.pk}, name: {self.name})'
    
    def __str__(self) -> str:
        return f'(id: {self.pk}, name: {self.name})'
