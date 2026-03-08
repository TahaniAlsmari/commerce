from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import User ,Listing ,Bid , Comment


def index(request):
    listings = Listing.objects.all()
    return render (request, "auctions/index.html" ,
    {"listing": listings }
    )

def create_listing(request):
    if request.method == 'POST':
        title = request.POST["title"]
        desc = request.POST["description"]
        price = request.POST["price"]
        image = request.POST["image"]
        cat = request.POST.get("category", "") 
        
        new_listing = Listing.objects.create(
            title = title,
            description = desc,
            starting_bid = price,
            image_url = image,
            category = cat,
            owner = request.user, 
            is_active = True
        )
        return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/create.html")

def toggle_watchlist(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    
    if request.user in listing.watchlist.all():
        listing.watchlist.remove(request.user)
    else:
        listing.watchlist.add(request.user)
    
    return HttpResponseRedirect(reverse("watchlist"))

def place_bid(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(id=listing_id)
        new_bid_input = request.POST.get("new_bid")
        
        if new_bid_input:
            new_bid_amount = float(new_bid_input)
            current_price = listing.starting_bid
            if new_bid_amount > current_price:
                Bid.objects.create(
                    amount=new_bid_amount, 
                    user=request.user, 
                    listing=listing
                )
                listing.starting_bid = new_bid_amount
                listing.save()
                messages.success(request, "Bid placed successfully!")
            else:
                messages.error(request, f"Your bid must be higher than ${current_price}")       
        return HttpResponseRedirect(reverse("listing_detail", args=(listing.id,)))

def close_auction(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(id=listing_id)
        if request.user == listing.owner:
            listing.is_active = False
            listing.save()
        return HttpResponseRedirect(reverse("listing_detail", args=(listing_id,)))
def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    
    highest_bid = Bid.objects.filter(listing=listing).order_by('-amount').first()
    
    winner = None
    if not listing.is_active and highest_bid:
        winner = highest_bid.user  

    return render(request, "auctions/detail.html", {
        "listing": listing,
        "winner": winner,  
        "highest_bid": highest_bid,
    })

def watchlist(request):
    
    watched_listings = Listing.objects.filter(watchlist=request.user)
    
    return render(request, "auctions/watchlist.html", {
        "listings": watched_listings 
    })

def add_comment(request, listing_id):
    if request.method == "POST":
        message = request.POST.get("comment") 
        listing = Listing.objects.get(id=listing_id)
        
        if message:
            Comment.objects.create(
                user=request.user, 
                listing=listing, 
                message=message
            )
            messages.success(request, "Comment added!")
        
        return redirect("listing_detail", listing_id=listing_id)
    
def categories(request):
    return render(request, "auctions/categories.html")

def category_detail(request, category_name):
   
    listings = Listing.objects.filter(category=category_name)
    return render(request, "auctions/categories.html", {
        "listing": listings,          
        "category_name": category_name
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
