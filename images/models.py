from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, blank=True)
    url = models.URLField(max_length=256)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name='images_created', on_delete=models.CASCADE)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
        related_name = 'images_liked', blank=True)

    class Meta:
        indexes = [
            models.Index(fields = ['-created'])
        ]
        ordering = ['-created']

    def save(self, *args, **kwargs):
        """
        ? overriding the native save method
        ? to slugify the title of the image 
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title