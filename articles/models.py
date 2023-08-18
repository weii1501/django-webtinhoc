from django.db import models

from tags.models import Tag
from topics.models import Topic
from users.models import CustomUser
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.
class Articles(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='articles')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    slug = models.TextField(blank=True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    publish= models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)
    cover = models.ImageField(upload_to='article_images', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
    num_comments = models.IntegerField(default=0)
    likes = models.ManyToManyField(CustomUser, blank=True, related_name='articles_liked')
    num_views = models.PositiveIntegerField(default=0)

    STATUS_THREAD_CHOICES = (
        ('C', 'Đang chờ'),
        ('P', 'Công khai'),
        ('B', 'Cấm'),
    )
    status = models.CharField(max_length=1, choices=STATUS_THREAD_CHOICES, default='C')

    def __str__(self):
        return self.title
    
    def save_with_id(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.title)}.{self.id}"
        super().save(*args, **kwargs)

    @property
    def total_likes(self):
        return self.likes.count()