from django.shortcuts import render
from contact.forms import Contact_usForm
from contact.models import Contact_us

# Create your views here.
def contact_home(request):
    if request.method == 'POST':
        fm = Contact_usForm(request.POST)
        if fm.is_valid():
            fn = fm.cleaned_data['first_name'] 
            ln = fm.cleaned_data['last_name']
            em = fm.cleaned_data['email']
            ms = fm.cleaned_data['message']
            print('####################################')
            print('first name = ', fm)
            print('last name = ', ln)
            print('email = ', em)
            print('meassage = ', ms)
            print('####################################')
            registered = Contact_us(first_name=fn, last_name=ln, email=em, message=ms) 
            registered.save()
            fm = Contact_usForm()
            return render(request, 'contact/contact_thanks.html')

        else:
            print('Data is not valid')
    else:
        fm = Contact_usForm()
        print('From get request')
    return render(request, 'contact/contact_home.html', {'form': fm})


def contact_thanks(request):
    return render(request, 'contact/contact_thanks.html',{})





