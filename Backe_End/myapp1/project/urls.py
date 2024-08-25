

from django.urls import path, include

from . import views



urlpatterns = [
    path('register', views.register),
    path('login', views.user_login),
    path('logout', views.logout_user),
    path ('profile', views.profile),
    path('add_product', views.add_product),
    path('getStore', views.getStore), ## product all
    path('getPhoto', views.getPhoto),
    path('product/<int:id>', views.getProductById),
    path('menuSearch/<str:category>',views.getMenuFilter),
    path('getMenu', views.getMenu),
    path('search/<str:product_name>', views.Search_Market),  ### 10 -rd funkcuia
    path('avatar', views.add_UserPhoto),
    path('change_username', views.update_username),
    path('changePassword', views.change),
    path('changeFirstName', views.update_first_name),
    path('changeLastName', views.update_last_name),
    path('changeMail', views.update_email),
    path('addCard', views.add_Cardproduct),
    path('getCard', views.getCard),
    path ('deleteCard/<int:id>', views.del_Card),


    ## 20 -rd funkcia
]