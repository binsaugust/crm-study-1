from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('page1/',views.page1,name='page1'),
    path('logout/',views.logout_user,name='logout_user'),
]
    