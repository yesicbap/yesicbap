from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import  DetailView
from django.http import Http404


from product.models import Product

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "product/product_home.html"
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 1


    def paginate_queryset(self, queryset, page_size):
        try:
            context = super(ProductListView,
                            self).paginate_queryset(queryset, page_size)
            return context
        except Http404:
            self.kwargs['page'] = 1
            context = super(ProductListView,
                            self).paginate_queryset(queryset, page_size)
            return context
            



class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_item.html"


