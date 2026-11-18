from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_restaurants, name="show_restaurants"),
    path("new/", views.new_restaurant, name="new_restaurant"),
    path("edit/<int:restaurant_id>/", views.edit_restaurant, name="edit_restaurant"),
    path("delete/<int:restaurant_id>/", views.delete_restaurant, name="delete_restaurant"),
    path("menus/<int:restaurant_id>/", views.show_menu_items, name="menu"),
    path("menus/<int:restaurant_id>/new/", views.new_menu_item, name="new_menu_item"),
    path(
        "menus/<int:restaurant_id>/edit/<int:item_id>/",
        views.edit_menu_item,
        name="edit_menu_item",
    ),
    path(
        "menus/<int:restaurant_id>/delete/<int:item_id>/",
        views.delete_menu_item,
        name="delete_menu_item",
    ),
]
