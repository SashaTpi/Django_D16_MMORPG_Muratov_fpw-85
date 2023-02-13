from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Reply
from django.template.loader import render_to_string


@receiver(post_save, sender=Reply)
def new_reply(sender, instance, created, **kwargs):
    if created:
        html_context = {'new_reply': instance, 'post': instance.post, }
        html_content = render_to_string('reply_to_post_author_mail.html', html_context)
        send_mail(
            subject='У Вас новый отклик на сайте MMORPG',
            message=None,
            html_message=html_content,
            from_email=None, # DEFAULT_FROM_EMAIL from settings.py
            recipient_list=[instance.post.author.email],
            fail_silently=False,
        )


@receiver(post_save, sender=Reply)
def reply_accepted(sender, instance, update_fields,  **kwargs):
    if update_fields and 'accept_status' in update_fields:
        html_context = {'reply': instance, 'post': instance.post, 'post_id': instance.id}
        html_content = render_to_string('accept_reply_mail.html', html_context)
        send_mail(
            subject='Ваш отклик на сайте MMORPG одобрен автором поста!',
            message=None,
            html_message=html_content,
            from_email=None,  # DEFAULT_FROM_EMAIL from settings.py
            recipient_list=[instance.post.author.email],
            fail_silently=False,
        )


