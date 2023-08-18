from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):

    name=models.CharField(max_length=500, verbose_name="Category")
    description=models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    num_posts = models.IntegerField(default=0)
    cover = models.ImageField(upload_to='category_images', blank=True, null=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children'
    )


    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)