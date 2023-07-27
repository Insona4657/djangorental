from django.urls import path, include
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
    path("sample", views.sample, name="sample"),
    path("account", views.account, name="account"),
    path("password-reset/", 
         auth_views.PasswordResetView.as_view(template_name='djangorental/password_reset.html'), 
         name="password_reset"),
    path("password-reset/done/", 
         auth_views.PasswordResetDoneView.as_view(template_name='djangorental/password_reset_done.html'), 
         name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", 
         auth_views.PasswordResetConfirmView.as_view(template_name='djangorental/password_reset_confirm.html'), 
         name="password_reset_confirm"),
    path("password-reset-complete/", 
         auth_views.PasswordResetCompleteView.as_view(template_name='djangorental/password_reset_complete.html'), 
         name="password_reset_complete"),
    
]
