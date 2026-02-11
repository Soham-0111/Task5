from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('add/', PostCreateView.as_view(), name='post_add'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
