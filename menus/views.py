from django.shortcuts import get_object_or_404, redirect, render

from .forms import MenuItemForm, RestaurantForm
from .models import MenuItem, Restaurant


def show_restaurants(request):
    restaurants = Restaurant.objects.order_by("name")
    return render(
        request,
        "restaurants/show_restaurants.html",
        {"restaurants": restaurants},
    )


def new_restaurant(request):
    form = RestaurantForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("show_restaurants")
    return render(request, "restaurants/new_restaurant.html", {"form": form})


def edit_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    form = RestaurantForm(request.POST or None, instance=restaurant)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("show_restaurants")
    return render(
        request,
        "restaurants/edit_restaurant.html",
        {"form": form, "restaurant": restaurant},
    )


def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == "POST":
        restaurant.delete()
        return redirect("show_restaurants")
    return render(
        request,
        "restaurants/delete_restaurant.html",
        {"restaurant": restaurant},
    )


def show_menu_items(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu_items = restaurant.menu_items.order_by("category", "name")
    return render(
        request,
        "menus/show_menu_items.html",
        {"restaurant": restaurant, "menu_items": menu_items},
    )


def new_menu_item(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    form = MenuItemForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        menu_item = form.save(commit=False)
        menu_item.restaurant = restaurant
        menu_item.save()
        return redirect("menu", restaurant_id=restaurant.id)
    return render(
        request,
        "menus/new_menu_item.html",
        {"form": form, "restaurant": restaurant},
    )


def edit_menu_item(request, restaurant_id, item_id):
    menu_item = get_object_or_404(
        MenuItem,
        pk=item_id,
        restaurant_id=restaurant_id,
    )
    form = MenuItemForm(request.POST or None, instance=menu_item)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("menu", restaurant_id=restaurant_id)
    return render(
        request,
        "menus/edit_menu_item.html",
        {"form": form, "menu_item": menu_item, "restaurant_id": restaurant_id},
    )


def delete_menu_item(request, restaurant_id, item_id):
    menu_item = get_object_or_404(
        MenuItem,
        pk=item_id,
        restaurant_id=restaurant_id,
    )
    if request.method == "POST":
        menu_item.delete()
        return redirect("menu", restaurant_id=restaurant_id)
    return render(
        request,
        "menus/delete_menu_item.html",
        {"menu_item": menu_item, "restaurant_id": restaurant_id},
    )
