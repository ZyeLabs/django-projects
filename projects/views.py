from django.views.generic.list_detail import object_list
from models import Project
 
def object_detail(request, slug):
    obj = Project.objects.filter(slug__exact=slug)
    return object_list(request, queryset=obj)