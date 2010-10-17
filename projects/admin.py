# Projects admin
from django.contrib import admin
from zyelabs.admin import BaseAdmin
from projects.models import Project, Technology, ProjectTechnology


admin.site.register(Project, BaseAdmin)
admin.site.register(Technology, BaseAdmin)
admin.site.register(ProjectTechnology)


