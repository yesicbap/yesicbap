from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import  DetailView
from django.http import Http404

from blog.models import Blog
# Create your views here.



class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_home.html"
    ordering = ['id']
    paginate_by = 6
    paginate_orphans = 1


    def paginate_queryset(self, queryset, page_size):
        try:
            context = super(BlogListView,
                            self).paginate_queryset(queryset, page_size)
            return context
        except Http404:
            self.kwargs['page'] = 1
            context = super(BlogListView,
                            self).paginate_queryset(queryset, page_size)
            return context



class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_item.html"




