from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createProduct/", views.createProduct, name="createProduct"),
    path("Product/<int:id>", views.product, name="product"),
    path("addComment/<int:id>", views.addComment, name="addComment"),
    path("displayCategory", views.displayCategory, name="displayCategory"),
    path("account", views.account, name="account"),
]