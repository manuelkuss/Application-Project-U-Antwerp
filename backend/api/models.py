from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MgfFile(models.Model):
    name = models.CharField(max_length=255)
    casanovo_file_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
