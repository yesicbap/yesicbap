from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def greet(request):
    return render(request, 'core/greet.html')



def error_404_view(request, *args, **argv):
    return render(request, 'core/404_page_not_found.html')

    
    