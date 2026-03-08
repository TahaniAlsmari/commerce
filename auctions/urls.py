from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("listing/<int:listing_id>/", views.listing_detail, name="listing_detail"),
    path("listing/<int:listing_id>/toggle", views.toggle_watchlist, name="toggle_watchlist"),
    path("listing/<int:listing_id>/bid", views.place_bid, name="place_bid"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listing/<int:listing_id>/add_comment", views.add_comment, name="add_comment"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category_name>", views.category_detail, name="category_detail"),
    path("close/<int:listing_id>", views.close_auction, name="close_auction"),
]
