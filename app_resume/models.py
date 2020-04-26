from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Resume(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = RichTextField(max_length=750, null=True)
    image = models.ImageField(null = True)
    link = models.CharField(max_length=70, null=True)

    def __str__(self):
        return "%s" % (self.title)

