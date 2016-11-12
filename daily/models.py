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
    votes = models.IntegerField()

    def __unicode__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('idea_edit', kwargs={'pk': self.pk})


class IdeaComment(models.Model):
    idea = models.ForeignKey(Ideas, null=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.TextField(max_length=50)
    comment = models.CharField(max_length=250)

class IdeaCategory(models.Model):
    idea = models.ForeignKey(Ideas, null=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=30)
