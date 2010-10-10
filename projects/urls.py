from django.conf.urls.defaults import *
from projects.models import Project, Technology

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^technology/$', 'object_list',
            { 'queryset': Technology.objects.all(),
            'template_name': 'projects/list.html',
            },
            name='technology_list'),
            
    url(r'^project/$', 'object_list',
            { 'queryset': Project.objects.all(),
            'template_name': 'projects/list.html',
            },
            name='project_list'),
    
    url(r'^technology/(?P<slug>[-\w]+)/$', 'object_detail',
            { 'queryset': Technology.objects.all(),
            'template_name': 'projects/detail.html',
            },
            name='technology_detail'),
            
    url(r'^project/(?P<slug>[-\w]+)/$', 'object_detail',
            { 'queryset': Project.objects.all(),
            'template_name': 'projects/detail.html',
            },
            name='project_detail'),
)