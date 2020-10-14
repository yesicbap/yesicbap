from django.contrib import admin
from contact.models import Contact_us

# Register your model here



@admin.register(Contact_us)
class Contact_usAdmin(admin.ModelAdmin):
    '''Admin View for Contact_us'''

    list_display = ('id', 'first_name','last_name', 'email', 'message')



