"""shoes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Shoeuniverse import views
from Shoeuniverse.views import MenView,WomenView,KidsView,NewArrivalView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signUp,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('newarrivals/',views.newArrivals,name='new-arrivals'),
    path('women/',views.women,name='women'),
    path('men/',views.men,name='men'),
    path('kids/',views.kids,name='kids'),
    path('menapi/',MenView.as_view()),
    path('womenapi/',WomenView.as_view()),
    path('kidsapi/',KidsView.as_view()),
    path('newarrivalsapi/',NewArrivalView.as_view()),
]
