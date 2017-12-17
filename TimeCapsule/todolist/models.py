# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create my models start #

class Task(models.Model):
    task_title = models.CharField(max_length=128)
    task_isCompleted = models.CharField(max_length=1, default='0')
    task_priority = models.CharField(max_length=1, default='0')

    def __unicode_(self):
        return u'%d %s %s' % (self.id, self.task_title, self.task_isCompleted)

    class Meta:
        ordering = ['task_priority']

# Create my models end #
