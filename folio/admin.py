from django.contrib import admin
from .models import Blog, Comment, Contact, Recommendation, Project, Tag
# Register your models here.
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Recommendation)
admin.site.register(Project)
admin.site.register(Tag)