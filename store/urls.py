from django.contrib import admin
from django.urls import path, include
from store.controller import authview, cart, wishlist, checkout, order
from store import views

urlpatterns = [
    
    path('',views.home,name="home"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),
    
    path('update_profile/', views.update_profile, name='update_profile'),
    
    path('product-list',views.productlistAjax ),
    path('searchproduct',views.searchproduct, name="searchproduct"),
    
    path('register/',authview.register, name="register"),
    path('login/',authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logoutpage"),
    
    
    path('add-to-cart',cart.addtocart, name="addtocart"),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart',cart.updatecart, name="updatecart" ),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),
    path('get_cart_count/', cart.get_cart_count, name='get_cart_count'),
    
    path('wishlist', wishlist.index, name="wishlist"),
    path('add-to-wishlist', wishlist.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item', wishlist.deletewishlistitem, name="deletewishlistitem"),
    
    path('checkout', checkout.index, name="checkout"),
    path('place-order', checkout.placeorder, name="placeorder"),
    
    path('proceed-to-pay', checkout.razorpaycheck),
    
    path('my-orders', order.index, name="myorders"),
    path('view-order/<str:t_no>',order.vieworder, name="orderview")
    
]