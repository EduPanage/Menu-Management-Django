from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem, Restaurant

# Restaurant Views

def show_restaurants(request):
    restaurants = Restaurant.objects.order_by('name')
    context = {'restaurants': restaurants}
    return render(request, "restaurants/show_restaurants.html", context)


def edit_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            restaurant.name = name
            restaurant.save()
            return redirect("show_restaurants") 
            
    return render(request, 'restaurants/edit_restaurant.html', {'restaurant': restaurant})


def show_menu_itens(request, restaurant_id):
    menu_itens = MenuItem.objects.filter(restaurant_id=restaurant_id).order_by('category')
    
    context = {'restaurant_id':restaurant_id, 'menu_itens': menu_itens}
    return render(request, "menus/show_menu_itens.html", context)


def new_menu_item(request, restaurant_id):
    
    if request.method == 'POST':
        form_data = request.POST
        menu_item = MenuItem()
        menu_item.category = form_data.get('category')
        menu_item.name = form_data.get('name')
        menu_item.description = form_data.get('description')
        menu_item.price = form_data.get('price')
        menu_item.restaurant_id = restaurant_id
        menu_item.save()
        
        return redirect(f"/menu/{restaurant_id}")
    
    else:
        return render(request, 'menus/new_menu_item.html', {'restaurant_id': restaurant_id})