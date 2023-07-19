from django.db import models
from django.contrib.auth.models import AbstractUser
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(AbstractUser):
    pass

"""class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    number = models.PhoneNumberField(null=False, blank=False, unique=True)
"""
class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.categoryName}"
    
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image_file = models.ImageField(null=True, blank=True, upload_to='images/', default='default.jpg')
    price = models.IntegerField(default=0)
    isActive = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")

    def __str__(self):
        return f"{self.title}, {self.description}, {self.price}"
    
class Comment(models.Model):
    comment_on_product = models.ForeignKey(Product,on_delete=models.CASCADE, blank=True, null=True, related_name="comment_on_product")
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="commenter")
    comment = models.CharField(max_length=300, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.commenter} has commented{self.comment} on {self.comment_on_product}"

    