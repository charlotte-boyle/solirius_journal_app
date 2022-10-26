from django.db import models


class Resource(models.Model):
    Name = models.CharField(max_length=50)
    Link = models.URLField()
