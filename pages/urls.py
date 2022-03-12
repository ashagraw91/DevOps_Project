from django.urls import path

#My Imports
from pages import views

urlpatterns = [
    path('', views.index, name = 'pages-index'),
]
