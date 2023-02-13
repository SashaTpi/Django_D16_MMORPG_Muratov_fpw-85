from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поста')
    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    text = RichTextUploadingField(blank=True, null=True, verbose_name='Сожержимое поста')
    categories = [
        ('tank', 'Танки'),
        ('healer', 'Хилы'),
        ('damage dealer', 'ДД'),
        ('vendor', 'Торговцы'),
        ('guildmaster', 'Гилдмастеры'),
        ('questgiver', 'Квестгиверы'),
        ('blacksmith', 'Кузнецы'),
        ('leatherworker', 'Кожевники'),
        ('potion maker', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    ]
    category = models.CharField(max_length=20, choices=categories)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост отклика')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор отклика')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата отклика')
    text = models.TextField(verbose_name='Содержимое отклика')
    accept_status = models.BooleanField(default=False, verbose_name='Принятие отклика')

    def __str__(self):
        return f'{self.author}: "{self.text}"'

    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'

