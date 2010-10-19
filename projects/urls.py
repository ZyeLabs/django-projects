from django.conf.urls.defaults import *
from projects.models import Project, Technology

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^technology/$', 'object_list',
            { 'queryset': Technology.objects.all(),
            'template_name': 'zyelabs/list.html',
            'extra_context': {'title': 'Technology' }
            },
            name='technology_list'),
            
    url(r'^project/$', 'object_list',
            { 'queryset': Project.objects.all(),
            'template_name': 'zyelabs/list.html',
            'extra_context': {'title': 'Projects' }
            },
            name='project_list'),
    
    url(r'^technology/(?P<slug>[-\w]+)/$', 'object_detail',
            { 'queryset': Technology.objects.all(),
            'template_name': 'zyelabs/detail.html',
            'extra_context': {'title': 'Technology' }
            },
            name='technology_detail'),
            
    url(r'^project/(?P<slug>[-\w]+)/$', 'object_detail',
            { 'queryset': Project.objects.all(),
            'template_name': 'zyelabs/detail.html',
            'extra_context': {'title': 'Projects' }
            },
            name='project_detail'),
)