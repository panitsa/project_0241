from django.contrib import admin
from django.contrib.auth.views import *
from django.views.generic.detail import *


class CustomLoginView(LoginView):
    template_name = 'admin/login.html' 

class EditView(DetailView):
    template_name = 'admin/add_edit.html'

class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'phone_number', 'image_url')
    template_name = 'admin/add_representative.html'