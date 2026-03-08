from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title =models.CharField(max_length=64)
    description=models.TextField()
    starting_bid=models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='paintings/')
    category=models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    is_active = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")

    def __str__(self):
        return f"{self.title}"
    
class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    listing=models.ForeignKey(Listing ,on_delete=models.CASCADE, related_name="listing_bids" )
    
    def __str__(self):
        return f"{self.amount} bid {self.user} on {self.listing}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments") 
    message = models.TextField()

    def __str__(self):
        return f"{self.user}: {self.message}"
    
