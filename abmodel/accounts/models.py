from django.db import models
# from product.models import ProductMainModel, ProductImageModel
class UserModel(models.Model):
    phone_number = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    is_customer = models.BooleanField(null=True,blank=True)
    is_admin = models.BooleanField(null=True,blank=True)
    
    def __int__(self):
        return self.phone_number 
    
    
class UserProfileModel(models.Model):
    choice = (('Male','Male'),('Female','Female'))
    owner = models.OneToOneField(UserModel,on_delete=models.CASCADE,related_name='owner1')
    name = models.CharField(max_length=23,null=True,blank=True)
    data_of_birth = models.DateTimeField(null=True,blank=True)
    gender = models.CharField(max_length=12,choices=choice)
    image = models.ImageField()
    
    def __str__(self):
        return self.name 
    
class UserLoginOtpModel(models.Model):
    owner = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='ownerw2')
    otp =    models.IntegerField(null=True,blank=True)
    active = models.BooleanField(null=True,blank=True)
    
    def __int__(self):
        return self.otp 
    
class UsercartProductModel(models.Model):
    choice = (('pending','pending'),('completed','completed'))
    owner = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='owner')
    # product = models.ForeignKey(ProductMainModel,on_delete=models.CASCADE,related_name='product1')
    status = models.CharField(max_length=15,choices=choice)
    
    def __str__(self):
        return self.status 
    

class UserCartModel(models.Model):
    owner = models.OneToOneField(UserModel,on_delete=models.CASCADE,related_name='owner3')
    product = models.ManyToManyField(UsercartProductModel)
    price = models.IntegerField(null=True,blank=True)
    
    def __int__(self):
        return self.price 