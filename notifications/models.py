from django.db import models
from users.models import CustomUser
from threads.models import Thread
# Create your models here.
class Notification(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_notifications')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_notifications')
    thread= models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='thread_notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message