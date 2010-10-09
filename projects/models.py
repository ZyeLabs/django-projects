# Project Models
from django.db import models
from zyelabs.models import Base, Image

class Project(Base):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    technologies = models.ManyToManyField('Technology', blank=True, null=True)
    image = models.ForeignKey(Image)

    class Meta:
        ordering = ['-start_date', '-end_date', ]

    def __unicode__(self):
        return self.title

class Technology(Base):
    image = models.ForeignKey(Image)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title