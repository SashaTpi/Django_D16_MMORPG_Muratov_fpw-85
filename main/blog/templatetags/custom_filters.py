from django import template
from blog.models import Reply

register = template.Library()


@register.filter(name='accept_reply_filter')
def accept_reply_filter(post_object):
    return Reply.objects.filter(post=post_object, accept_status=True)


@register.filter(name='notaccept_reply_filter')
def notaccept_reply_filter(post_object):
    return Reply.objects.filter(post=post_object, accept_status=False)
