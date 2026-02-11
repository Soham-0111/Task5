from django.views import View
from django.views.generic import DetailView
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


class PostListView(View):
    def get(self, request):
        all_posts = Post.objects.all()
        context = {'all_posts': all_posts}
        return render(request, 'blog/post_list.html', context)


class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        return render(request, 'blog/post_form.html', {'form': form})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
