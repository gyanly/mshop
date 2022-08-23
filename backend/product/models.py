from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name="Products")
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    cover_image = models.ImageField()
    status = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="ProductImages")
    image = models.ImageField()

    def __str__(self):
        return str(self.product)
    
     
