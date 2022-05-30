from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='movie'),
    path('tables/', views.tables),
    path('search/', views.search, name='search'),
    path('tag/', views.genre_tags, name='genre_tags'),
    path('<int:id>', views.movie_detail, name='movie_detail'),
    path('favorites/', views.favorites, name='favorites'),
]
