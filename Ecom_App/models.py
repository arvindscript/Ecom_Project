from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class All_Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Latest_Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name



class Blog_Product(models.Model):
    date = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Festival_Deals(models.Model):
    date = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name