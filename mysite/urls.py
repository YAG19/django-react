from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render


def index_view(request):
    return render(request, 'build/index.html')

urlpatterns = [

    path('',index_view,name="home"),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
