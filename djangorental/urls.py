from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createProduct/", views.createProduct, name="createProduct"),
    path("Product/<int:id>", views.product, name="product"),
    path("addComment/<int:id>", views.addComment, name="addComment"),
    path("category", views.displayCategory, name="displayCategory"),
    path("account", views.account, name="account"),
    path("password-reset/", 
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
         name="password_reset"),
    path("password-reset/done/", 
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
         name="password_reset_done"),
]