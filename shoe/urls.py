
from django.urls import path
from shoe import views
urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('signup/', views.signUp,name='signup'),
    path('logout/', views.logout,name='logout'),
    path('men/', views.men,name='men'),
    path('women/', views.women,name='women'),
    path('kids/', views.kids,name='kids'),
    path('newArrivals/', views.newArrivals,name='newArrivals'),
    path('<url>/order/<id>',views.orderSummary,name='ordersummary'),
    path('search',views.search,name='search'),
    path('orders/',views.importOrders,name='orders'),
    path('orders/<id>',views.cancelOrder,name='cancelOrder'),
    path('addToCart/<id>',views.addToCart,name='addToCart'),
    path('cart/',views.importCart,name='cart'),
    path('cart/<id>',views.removeCart,name='removecart') 
]