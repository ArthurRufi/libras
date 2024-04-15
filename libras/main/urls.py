from django.contrib import admin
from django.urls import path, include
from .views import n, link, tutotial, sinais



app_name = 'main'


urlpatterns = [
    path('', n, name='main'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('curso/<int:cod>', link, name='linkreturn'),
    path('tutorial/', tutotial, name = 'tutorial'),
    path('curso/<int:curso>/<int:sinal>', sinais),
]