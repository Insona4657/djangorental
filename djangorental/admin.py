from django.contrib import admin
from . models import Product, Category, User, Comment, UserProfile

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(UserProfile)