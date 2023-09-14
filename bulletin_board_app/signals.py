from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Comment

@receiver(post_save, sender=Comment)
def notify_about_new_comment(sender, instance, created, **kwargs):
    if created:
        subject = f'noreply. BulletinBoard: "You have a new comment."'
        message = f'You have a new comment from {instance.author.username} on your post - "{instance.post}": "{instance.text}"'
        email = instance.post.author.email
        send_mail(subject=subject, message=message, from_email=None, recipient_list=[email,])

@receiver(post_save, sender=Comment)
def notify_about_new_comment(sender, instance, created, **kwargs):
    if not created:
        subject = f'noreply. BulletinBoard: "Your comment has been accepted."'
        message = f'Your comment on post: "{instance.post}" has been accepted'
        email = instance.author.email
        send_mail(subject=subject, message=message, from_email=None, recipient_list=[email,])