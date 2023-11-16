from django.db import models


class Content(models.Model):
    bab = models.TextField(blank=True, null=True)
    title_1 = models.TextField(db_column='title 1', blank=True, null=True)
    title_2 = models.TextField(db_column='title 2', blank=True, null=True)
    title_3 = models.TextField(db_column='title 3', blank=True, null=True)
    type = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)


