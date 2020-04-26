from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Donatepage(models.Model):
    text = RichTextField(max_length = 1500, null = True)
    link = models.CharField(max_length = 150, null = True)
    need = models.PositiveIntegerField(null = True, blank = True)
    project = models.CharField(max_length = 250, null = True, blank = True)
    daonated = models.PositiveIntegerField(null = True, default = 0)