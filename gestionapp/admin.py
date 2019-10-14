from django.contrib import admin

# Register your models here.
from .models import Subscriber

admin.site.register(Subscriber)

class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'