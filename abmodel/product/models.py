from django.db import models

class ProductMainModel(models.Model):
    title = models.CharField(max_length=25,null=True,blank=True)
    descriptions = models.CharField(max_length=100,null=True,blank=True)
    unique_id = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    
    def __int__(self):
        return self.unique_id
    

class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductMainModel,on_delete=models.CASCADE,related_name='product4')
    image = models.ImageField() 