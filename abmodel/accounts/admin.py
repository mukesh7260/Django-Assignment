from django.contrib import admin
from accounts.models import * 

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','phone_number','email','is_customer','is_admin']
    
@admin.register(UserProfileModel) 
class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id','owner','name','data_of_birth','gender','image']
    
@admin.register(UserLoginOtpModel)
class UserLoginOtpModelAdmin(admin.ModelAdmin):
    list_display = ['id','owner','otp','active']
    
@admin.register(UsercartProductModel)
class UsercartProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','owner','status']
    
@admin.register(UserCartModel)
class UserCartModelAdmin(admin.ModelAdmin):
    list_display = ['id','owner','price']
    
    