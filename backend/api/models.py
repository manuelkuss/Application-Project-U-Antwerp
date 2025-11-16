import json

import numpy as np
from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class ChartData(models.Model):
#     title = models.CharField(max_length=100)
#     # data = models.TextField()
#
#     def __str__(self):
#         return self.title

class MgfFile(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Sequence(models.Model):
    title = models.CharField(max_length=255)
    sequence = models.TextField(default="")

    def __str__(self):
        return self.title