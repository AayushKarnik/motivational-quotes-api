from django.contrib import admin
from django.urls import path
from messagegenerator import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
