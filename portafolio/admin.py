from django.contrib import admin
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    #muestra los campos en el administrador
    readonly_fields = ('created','updated')

admin.site.register(Project,ProjectAdmin)