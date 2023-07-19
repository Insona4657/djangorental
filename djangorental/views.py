from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import User, Category, Product, Comment

def addComment(request, id):
    name = Product.objects.get(pk=id)
    commentdata = request.POST["newComment"]
    user = request.user
    newComment=Comment(
        commenter=user,
        comment_on_product=name,
        comment=commentdata
    )

    newComment.save()
    return HttpResponseRedirect(reverse('Product',args=(id, )))

def displayCategory(request):
    if request.method == "POST":
        categoryselected = request.POST['category']
        category = Category.objects.filter(type=request.POST['category'])
        activeproduct = Product.objects.filter(isActive=True, category=category)
        allCategories = Category.objects.all()
        return render(request, "djangorental/category.html", {
            "categories": allCategories,
            "products": activeproduct
        })
    else:
        activeproduct = Product.objects.filter(isActive=True)
        allCategories = Category.objects.all()
        return render(request, "djangorental/category.html", {
            "categories": allCategories,
            "products": activeproduct
        })


def createProduct(request):
    if request.method=="GET":
        allCategories = Category.objects.all()
        return render (request, "djangorental/createProduct.html", {
            "categories": allCategories
        })
    else:
        #Get Data from form
        name = request.POST["name"]
        description = request.POST["description"]
        image_url = request.POST["image"]
        price = request.POST["price"]
        user = request.user
        category = request.POST.get("category")
        bid = request.POST["bid"]

        #Get all content about particular category
        categoryData = Category.objects.get(type=category)

        #Create a new Product object
        newProduct = Product(
            name=name,
            description=description,
            imageUrl=image_url,
            price=float(price),
            owner=user,
            category=categoryData,
            bid= bid,
        )

        newProduct.save()
        return HttpResponseRedirect(reverse(index))


def index(request):
    activeProduct = Product.objects.filter(isActive=True)
    allCategories = Category.objects.all()
    return render(request, "djangorental/index.html", {
        "products": activeProduct,
        "categories": allCategories
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "djangorental/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "djangorental/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        address = request.POST["address"]
        number = request.POST["number"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "djangorental/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, address, number)
            user.save()
        except IntegrityError:
            return render(request, "djangorental/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "djangorental/register.html")
    
def product(request, id):
    name = product.objects.get(pk=id)
    isProductinWatchlist = request.user in name.watchlist.all()
    allComments = Comment.objects.filter(comment_on_product=name)
    isOwner = request.user == name.owner
    currentuserusername = request.user.username

    return render(request, "djangorental/product.html", {
        "product": name,
        "allComments": allComments,
        "isOwner": isOwner,
        "currentuserusername": currentuserusername,
    })

def account(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        address = request.POST["address"]
        number = request.POST["number"]

        # Update User Details
        """try:
            profile = UserProfile.objects.create_user(username, email, address, number)
            user.save()
        except IntegrityError:
            return render(request, "djangorental/account.html", {
                "message": "Username already taken."
            })"""
    else:
        currentuserusername = request.user.username
        currentuseremail = request.user.email
    return render(request, "djangorental/account.html", {
        "username" : currentuserusername,
        "email" : currentuseremail        
    })