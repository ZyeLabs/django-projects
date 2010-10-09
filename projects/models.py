# Project Models
from django.db import models
from zyelabs.models import Base, Image
from technologies.models import Technology

class Project(Base):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    technologies = models.ManyToManyField(Technology)
    image = models.ForeignKey(Image)

    class Meta:
        ordering = ['-start_date', '-end_date', ]

    def __unicode__(self):
        return self.title
