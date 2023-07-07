from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    #food/
    path('', views.Indexclassviews.as_view(), name="index" ),
    #food/item/
    path('item/', views.item, name="item" ),
    #food/1
    path('<int:item_id>/', views.detail, name="detail"),
    #add item
    path('add', views.CreateItem.as_view(), name="create_item"),
    # edit item
    path('edit/<int:id>/', views.edit_item, name="edit_item"),
    #delete item
    path('delete/<int:id>/', views.delete_item, name="delete_item"),
]
