from django.contrib import admin
from .models import AboutPage, ContactPage, Student, Notice, Teacher

admin.site.register(AboutPage)
admin.site.register(ContactPage)
admin.site.register(Student)
admin.site.register(Notice)
admin.site.register(Teacher)
