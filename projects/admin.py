# Projects admin
from django.contrib import admin
from projects.models import Project, Technology

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','url','short_description')

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title','url','short_description')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)


