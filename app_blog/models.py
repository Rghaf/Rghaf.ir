from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
import jdatetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 50, null = True)
    slug = models.SlugField(null = True, blank = False)
    main_content = RichTextField(max_length = 2500, null = True)
    summary = models.CharField(max_length = 350, null = True)
    image = models.ImageField(null = True, blank = True, upload_to = 'images/%Y/%m/%d/')
    category = models.ForeignKey("app_blog.Category", null = True, blank = False, on_delete=models.CASCADE)
    dl_btn = models.CharField(max_length = 250, null = True, blank = True)
    date =  models.DateTimeField(null = True, auto_now_add = True)
    #music-player

    def jd_date(self):
        jdatetime.set_locale('fa_IR')
        jdatetime.datetime.now().strftime('%A %B')
        jd_datetime = jdatetime.datetime.fromgregorian(
            year = self.date.year,
            month = self.date.month,
            day = self.date.day,
            hour = self.date.hour,
            minute = self.date.minute,
            second = self.date.second,
        )
        return jd_datetime.strftime('%A, %d %B %Y ساعت %H:%M')

    def get_absolute_url(self):
        return "/post/%s" % self.slug

    def img_404(self):
        return settings.POST_404

    def __str__(self):
        return "%s - %s : %s" % (self.id, self.title, self.summary )

class Category(models.Model):
    title = models.CharField(max_length=50, null = True)
    slug = models.SlugField(null = True, blank = False)
    description = models.CharField(max_length=150, null = True)

    def get_absolute_url(self):
        return "/category/%s" % self.slug

    def __str__(self):
        return self.title
    

class Slider(models.Model):
    description = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=150, null = True, blank = True)
    image = models.ImageField(null = True, blank = True, upload_to= 'images/slider')

    def img_404(self):
        return settings.SLIDE_404
    
    def __str__(self):
        return self.description


    


