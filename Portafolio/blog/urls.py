from django.urls import URLPattern, path

from .views import render_posts

urlpattern = [
    path('', render_posts, name='posts'),
]
