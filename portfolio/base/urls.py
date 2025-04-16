
from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'base'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home/', views.home,name="home"),
]
