from django.db import models
from django.conf import settings 
from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.urls import reverse

from django.core.files.storage import default_storage
from io import BytesIO
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)
    body = RichTextUploadingField()
    blockquote = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='blog/%Y/%m/', null=True, blank=True)
    credit = models.CharField(max_length=120)
    featured = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=120,
    )

    def __str__(self):
        return f'{self.title} on {self.published}'
        

    class Meta:
        unique_together = ('title', 'slug')

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('single', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Comment(models.Model):
    
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    writer = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=120)
    website = models.CharField(max_length=120, blank=True, null=True)
    body = models.TextField()
    active = models.BooleanField(default=True)
    published = models.DateTimeField(auto_now_add=True)
    def __str__(self):

        return "{} commented on {}".format(self.writer,self.published)

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    subject = models.CharField(max_length=750)
    message = models.TextField()
    date_stamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} contacted on {}".format(self.name,self.date_stamp)


class Project(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=150)
    link = models.CharField(max_length=250)
    image = models.ImageField(upload_to='works/')
    date_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Recommendation(models.Model):
    name = models.CharField(max_length=120)
    recommendation = models.CharField(max_length=1500)
    image = models.ImageField(default = 'default.png', upload_to='recommendations/%Y/%m/', null=True, blank=True)
    active = models.BooleanField(default=False)
    date_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} recommended on {self.date_stamp}'
    
    # def save(self, *args, **kwargs):
    #     #run save of parent class above to save original image to disk
    #     super().save(*args, **kwargs)

    #     memfile = BytesIO()

    #     img = Image.open(self.image)
    #     if img.height > 150 or img.width > 150:
    #         output_size = (150, 150)
    #         img.thumbnail(output_size, Image.ANTIALIAS)
    #         img.save(memfile, 'JPEG', quality=95)
    #         default_storage.save(self.image.name, memfile)
    #         memfile.close()
    #         img.close()
    
