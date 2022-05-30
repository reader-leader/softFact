from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from .forms import CommentForm
from . models import *
from . form import MovieForm


def index(request):
    ff = Movies.objects.all()
    genres = Genre.objects.all()
    return render(request, 'main/index.html', {'ff': ff, 'genres': genres})


def movie_detail(request, id):
    post = get_object_or_404(Movies, pk=id)

    if request.user.is_authenticated:
        post.favorites.add(request.user)
        return render(request, 'main/details.html', {'post': post})
    else:
        submitted = False
        if request.method == "POST":
            post = CommentForm(request.POST, instance=post)
            com = Comments.object.all()
            if post.is_valid():
                post.save()
                return redirect('movie_detail', 'submitted=True', {'com': com}, pk=post.id)

        return render(request, 'main/details.html', {'post': post, 'submitted': submitted})


# def favorites_add(request, id):
#     fav_add = get_object_or_404(Movies, pk=id)
#     fav_add.favorites_add.add(request.user)
#     return render(request, 'main/details', {'fav_add': fav_add})

#
# def comments(request):
#     submitted = False
#     if request.method == "POST":
#         comments = CommentForm(request.POST)
#         if comments.is_valid():
#             comments.save()
#         return redirect('main/details.html', 'submitted=True')
#     else:
#         forms = CommentForm()
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'main/details.html', {'form': forms, 'submitted': submitted})



def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        movies = Movies.objects.filter(title__contains=searched)
        return render(request, 'main/search.html', {'searched': searched, 'movies': movies})
    else:
        return render(request, 'main/search.html')


def genre_tags(request):
    if request.method == "POST":
        search_by_tags = request.POST['search_by_tags']
        genre = Genre.objects.filter(tags__name__in=search_by_tags)
        return render(request, 'main/search_by_tags.html', {'search_by_tags': search_by_tags, 'genre': genre})
    else:
        return render(request, 'main/search_by_tags.html')


def favorites(request):
    user = request.user
    fav = user.favorites.all()
    return render(request, 'main/favorites.html', {'fav': fav})


def tables(request):
    tables = User.objects.all()
    # novels = Novel.objects.all()
    # return render(request, 'main/table.html', {'tables': tables, 'novels': novels})
