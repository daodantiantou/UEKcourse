# from django.contrib import admin
from django.urls import path
from . import views

app_name='courseIndex'

urlpatterns = [
    path('', views.index,name='index'),
    path('predictCourser/', views.predictCourser,name='predictCourser'),
    path('getbeforecourse/<week>',views.getbeforecourse,name='getbeforecourse' ),
    path('getnextcourse/<week>',views.getnextcourse,name='getnextcourse' ),
    path('getstage/<classname>',views.getstage,name='getstage' ),
    path('getteacher/<classname>/<stagename>',views.getteacher,name='getteacher' ),
    path('savedata/', views.savedata, name='savedata'),
]