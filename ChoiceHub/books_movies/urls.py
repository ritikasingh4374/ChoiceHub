"""
URL configuration for ChoiceHub project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from books_movies import views
from .views import register
# from .views import book_recommendation

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.book_list, name='book_list'),
    path('register/', register, name='register'),

    # path('quiz/', book_recommendation, name='book_recommendation'),
]