from django.urls import path
from .views import index, single, search_view, TagPostListView, PostListView, recommend


urlpatterns = [
    path('', index, name='index'),
    path('blog/<int:pk>-<str:slug>/', single, name='single'),
    #path('blog/', blog, name='blog'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('search/', search_view, name='search'),
    path('category/<str:name>', TagPostListView.as_view(), name='tag'),
    path('recommend/', recommend, name='recommend')
    
]