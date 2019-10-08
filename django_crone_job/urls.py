from django.contrib import admin
from django.urls import path
from crone_job import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('crone/', views.crone, name="crone")
]
