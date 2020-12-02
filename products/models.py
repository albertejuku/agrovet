from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    prod_cats = (
        ('AN', 'animal feeds'),
        ('FZ', 'fertilizers'),
        ('SD', 'seeds'),
        ('AC', 'farm accesories')
    )

    name = models.CharField(max_length=100)
    description = models.TextField()    
    price = models.IntegerField()
    MOQ = models.IntegerField(null=True)
    stock = models.IntegerField()
    category = models.CharField(max_length=2, choices=prod_cats)
    date_created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='media/')

    def __str__(self):
        return f'{self.name} ..{self.category}'

    def get_absolute_url(self):
        return u'/home/product/%d' % self.pk
