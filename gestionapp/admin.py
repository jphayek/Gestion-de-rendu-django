from django.contrib import admin

# Register your models here.
from .models import Subscriber
from .models import Teacher
from .models import Student
from .models import Project
from .models import ProjectGroup
admin.site.register(Subscriber)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(ProjectGroup)

class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'