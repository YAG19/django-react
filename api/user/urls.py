# basic URL Configurations
from django.urls import include, path
from rest_framework import routers
from . import views
  
  
# define the router
router = routers.DefaultRouter()
  
# define the router path and viewset to be used
router.register(r'', views.UserViewSet)
  
# specify URL Path for rest_framework
urlpatterns = [
    path('login/', views.userlogin , name='login'),
    path('', include(router.urls)),
    ]