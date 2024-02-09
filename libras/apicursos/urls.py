from django.contrib import admin
from django.urls import path, include
from .views import apichamar


app_name = 'apicursos'


urlpatterns = [
    path('', apichamar, name='chamar')

]