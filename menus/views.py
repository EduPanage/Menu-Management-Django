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


# Menu Item Views

def show_menu_itens(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu_itens = MenuItem.objects.filter(restaurant=restaurant).order_by('category')
    
    context = {
        'restaurant': restaurant,
        'restaurant_id': restaurant.id, # Mantido para compatibilidade com seu template
        'menu_itens': menu_itens
    }
    return render(request, "menus/show_menu_itens.html", context)


def new_menu_item(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    
    if request.method == 'POST':
        form_data = request.POST
        price = form_data.get('price', '0').replace(',', '.').strip()
        
        menu_item = MenuItem()
        menu_item.category = form_data.get('category', '').strip()
        menu_item.name = form_data.get('name', '').strip()
        menu_item.description = form_data.get('description', '').strip()
        menu_item.price = price
        menu_item.restaurant = restaurant
        menu_item.save()
        
        return redirect("show_menu_itens", restaurant_id=restaurant.id)
    
    return render(request, 'menus/new_menu_item.html', {
        'restaurant': restaurant,
        'restaurant_id': restaurant.id
    })

    
def new_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            Restaurant.objects.create(name=name)
            return redirect("/")
        
    return render(request, 'restaurants/new_restaurant.html')


def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    
    if request.method == 'POST':
        restaurant.delete()
        return redirect("/")
        
    return render(request, 'restaurants/delete_restaurant.html', {'restaurant': restaurant})


# Edição de Item do Cardápio
def edit_menu_item(request, restaurant_id, item_id):
    menu_item = get_object_or_404(MenuItem, pk=item_id, restaurant_id=restaurant_id)
    
    if request.method == 'POST':
        form_data = request.POST
        price = form_data.get('price', '0').replace(',', '.').strip()
        
        menu_item.category = form_data.get('category', '').strip()
        menu_item.name = form_data.get('name', '').strip()
        menu_item.description = form_data.get('description', '').strip()
        menu_item.price = price
        menu_item.save()
        
        return redirect("menu", restaurant_id=restaurant_id)
        
    return render(request, 'menus/edit_menu_item.html', {
        'restaurant_id': restaurant_id,
        'menu_item': menu_item
    })


# Exclusão de Item do Cardápio
def delete_menu_item(request, restaurant_id, item_id):
    menu_item = get_object_or_404(MenuItem, pk=item_id, restaurant_id=restaurant_id)
    
    if request.method == 'POST':
        menu_item.delete()
        return redirect("menu", restaurant_id=restaurant_id)
        
    return render(request, 'menus/delete_menu_item.html', {
        'restaurant_id': restaurant_id,
        'menu_item': menu_item
    })