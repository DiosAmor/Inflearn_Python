from typing import Any
from django.db import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post

# post_list = login_required(ListView.as_view(model=Post,paginate_by=10))

@method_decorator(login_required, name = 'dispatch')
class PostListView(ListView):
    model = Post
    paginate_by=10

post_list = PostListView.as_view()

# # Create your views here.
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q','')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html
#     return render(request,'instagram/post_list.html',{
#         'post_list':qs,
#         'q':q,
#     })
    
# def post_detail(request: HttpRequest,pk:int)->HttpResponse:
#     post = get_object_or_404(Post,pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     return render(request,'instagram/post_detail.html',{
#         'post':post,
#     })

# post_detail = DetailView.as_view(
#     model=Post,
#     queryset=Post.objects.filter(is_public=True)
# )

class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public = True)
    
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

post_detail = PostDetailView.as_view()

# def archives_year(request,year):
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', paginate_by=10)