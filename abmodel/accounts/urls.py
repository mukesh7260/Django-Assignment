from django.contrib import admin
from django.urls import path , include 
from accounts import views 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/<int:pk>/',views.Details.as_view()),
    
]