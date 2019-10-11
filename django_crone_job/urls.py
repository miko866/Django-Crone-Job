from django.contrib import admin
from django.urls import path
from crone_job import views


# Work only DEBUG=False
handler_404 = 'crone_job.views.handler_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('crone/', views.crone, name="crone"),
    path('entries/', views.entries, name="entries"),
]
