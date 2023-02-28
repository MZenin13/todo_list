from colorfield.fields import ColorField
from django.db import models


class Note(models.Model):
    caption = models.CharField(max_length=250)
    content = models.TextField()
    reminder_time = models.DateTimeField(blank=True, null=True)
    tag = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.caption

    def tags(self):
        return self.tag.all().values()


class Tag(models.Model):
    name = models.CharField(max_length=250)
    color = ColorField(blank=False)

    def __str__(self):
        return self.name
