from django.conf.urls.defaults import *
from projects.models import Project, Technology

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$', 'object_list',
            { 'queryset': Project.objects.all(),
            'template_name': 'projects/list.html',
            },
            name='project_list'),
    url(r'^(?P<slug>[-\w]+)/$', 'object_detail',
            { 'queryset': Project.objects.all(),
            'template_name': 'projects/detail.html',
            },
            name='project_detail'),
)