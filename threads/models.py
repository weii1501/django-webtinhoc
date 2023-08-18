from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify

from tags.models import Tag
from topics.models import Topic
from users.models import CustomUser


# Create your models here.
class Thread(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='threads')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='threads')
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255,blank=True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    publish= models.BooleanField(default=True)

    STATUS_THREAD_CHOICES = (
        ('C', 'Đang chờ'),
        ('P', 'Công khai'),
        ('B', 'Cấm'),
    )
    status = models.CharField(max_length=1, choices=STATUS_THREAD_CHOICES, default='C')
    tags = models.ManyToManyField(Tag, related_name='threads')
    likes = models.ManyToManyField(CustomUser, related_name='threads_liked', blank=True)
    num_views = models.PositiveIntegerField(default=0)
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def tags_names(self):
        return [str(tags.name) for tags in self.tags.all()]
    
    def save_with_id(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.title)}.{self.pk}"
        if not self.publish:
            self.publish=True
        return super().save(*args, **kwargs)

    @property
    def get_total_likes(self):
        return self.likes.count()

    @property
    def get_total_replies(self):
        return self.replies.count()

    @property
    def get_total_participants(self):
        return self.replies.values('user').distinct().count()

    @property
    def get_last_reply(self):
        return self.replies.order_by('-created_at').first()
