from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

from django.core.urlresolvers import reverse


class Ideas(models.Model):
    idea_id = models.AutoField(primary_key=True)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('idea_edit', kwargs={'pk': self.pk})


