from celery import shared_task
from .models import Post, User
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from mmorpg.settings import DEFAULT_FROM_EMAIL


@shared_task
def action():
    new_posts = Post.objects.filter(article_time_in__gt=datetime.now() - timedelta(days=7))
    list_of_emails = []
    for user in User.objects.all():
        list_of_emails.append(user.email)
    html_context = {'new_posts': new_posts}
    html_content = render_to_string('week_posts_mail.html', html_context)
    msg = EmailMultiAlternatives(
        subject='Новые объявления на сайте MMORPG',
        from_email=DEFAULT_FROM_EMAIL,
        to=list_of_emails
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()

