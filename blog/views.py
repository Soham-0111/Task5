from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import render
from .models import Post

class PostListView(View):
    def get(self, request):
        all_posts = Post.objects.all()
        context = {'all_posts': all_posts}
        return render(request, 'blog/post_list.html', context)
