from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Comment

@receiver(post_save, sender=User)
def create_comment(sender, instance, created, **kwargs):
    if created:
        Comment.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_comment(sender, instance, **kwargs):
    instance.Comment.save()
