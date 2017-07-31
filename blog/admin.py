from django.contrib import admin
from .models import Post #makes it include the models post we made


# Register your models here.

#this will make it visible on the admin page
admin.site.register(Post)
