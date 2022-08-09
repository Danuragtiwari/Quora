from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views
app_name="app"
urlpatterns = [
    path('admin/', admin.site.urls),
   # login
]