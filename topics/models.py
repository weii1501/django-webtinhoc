from django.db import models
from catergories.models import Category
from users.models import CustomUser
from django.utils.text import slugify

# Create your models here.
class Topic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='topics')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100 ,blank=True)
    cover = models.ImageField(upload_to='topic_images', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.title)}"
        super().save(*args, **kwargs)