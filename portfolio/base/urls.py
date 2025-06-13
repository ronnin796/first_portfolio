
# This code snippet is defining URL patterns for a Django web application. Here's a breakdown of what
# each part does:
from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'base'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home/', views.home,name="home"),
    path('education/', views.education,name="education"),
    path('skills/', views.skills , name="skills"),

]
