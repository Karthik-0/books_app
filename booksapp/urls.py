"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views


urlpatterns = [
    path('', views.BookList.as_view(), name='index'),
    path('detail/<int:pk>', views.BookDetail.as_view(), name='detail'),
    path('add/', views.BookAdd.as_view(), name='create'),
    path('genre/', views.GenreList.as_view(), name='genre'),
    path('genre/<int:pk>', views.GenreEdit.as_view(), name='genre_edit'),
    path('genre/<int:pk>/delete', views.GenreDelete.as_view(),
         name='genre_delete'),
    path('author/', views.AuthorList.as_view(), name='author'),
    path('author/<int:pk>', views.AuthorEdit.as_view(), name='author_edit'),
    path('author/<int:pk>/delete', views.AuthorDelete.as_view(),
         name='author_delete'),
    path('edit/<int:pk>', views.BookUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.BookDelete.as_view(), name='delete'),
]
