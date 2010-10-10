# Projects admin
from django.contrib import admin
from projects.models import Project, Technology

class BaseAdmin(admin.ModelAdmin):
    list_display = ('title','url','short_description')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project, BaseAdmin)
admin.site.register(Technology, BaseAdmin)


