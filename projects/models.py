# Project Models
from django.db import models
from zyelabs.models import Base, Image
from photologue.models import Gallery

class Project(Base):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    technologies = models.ManyToManyField('Technology', blank=True, null=True, through='ProjectTechnology')
    image = models.ForeignKey(Image)
    gallery = models.ForeignKey(Gallery, null=True, blank=True)

    class Meta:
        ordering = ['-start_date', '-end_date', ]

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('project_detail', (), {"slug": self.slug})

class Technology(Base):
    image = models.ForeignKey(Image)
    projects = models.ManyToManyField('Project', blank=True, null=True, through='ProjectTechnology')

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('technology_detail', (), {"slug": self.slug})

class ProjectTechnology(models.Model):
    technology = models.ForeignKey(Technology)
    project = models.ForeignKey(Project)