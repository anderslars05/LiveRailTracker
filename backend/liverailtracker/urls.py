from django.contrib import admin
from django.urls import path
from apps.home import views  # import views from the home app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
]
