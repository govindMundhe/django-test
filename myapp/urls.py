from django.urls import path , include
from . import views
urlpatterns = [
    path('new_order', views.Neworder ,name = 'new order'),
    path('index', views.index ,name = 'orders'),
    path('new_item', views.Additem ,name = 'Add item'),
    path('index_items', views.index_items ,name = 'Menu'),

]