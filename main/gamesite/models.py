from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
import datetime


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Название')

    def __str__(self):
        return f'{self.name}'


class Note(models.Model):
    TANKS = 'tanks'
    HEALERS = 'healers'
    DD = 'damage dealers'
    MERCHANTS = 'merchants'
    GUILD_MASTER = 'guild masters'
    QUEST_GIVERS = 'questgivers'
    BLACKSMITH = 'blacksmiths'
    LEATHERWORKERS = 'leatherworkers'
    POTION_MAKERS = 'potions makers'
    SPELL_MASTERS = 'spell masters'

    CATEGORIES = [
        (TANKS, 'tanks'),
        (HEALERS, 'healers'),
        (DD, 'damage dealers'),
        (MERCHANTS, 'merchants'),
        (GUILD_MASTER, 'guild masters'),
        (QUEST_GIVERS, 'questgivers'),
        (BLACKSMITH, 'blacksmiths'),
        (LEATHERWORKERS, 'leatherworkers'),
        (POTION_MAKERS, 'potions makers'),
        (SPELL_MASTERS, 'spell masters'),
    ]

    title = models.CharField('Title ', max_length=128)
    header_image = models.FileField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    post_date = models.DateTimeField('Publication date ', auto_now_add=True)
    body = RichTextUploadingField('Text', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORIES, default=TANKS)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return f'{self.title}  |  {self.author}  |  {self.post_date}  |  {self.category}  |  {self.body[:64]}'

    def get_absolute_url(self):
        return reverse("article-detail", args=(str(self.id)))

    def get_categories(self):
        cat_menu = [
            'tanks',
            'healers',
            'damage dealers',
            'merchants',
            'guild masters',
            'questgivers',
            'blacksmiths',
            'leatherworkers',
            'potions makers',
            'spell masters',
        ]
        return cat_menu


class Response(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, verbose_name='Объявление')
    user_response = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор отклика')
    content = models.TextField(verbose_name='Контент отклика')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата отклика') #datetime
    status_del = models.BooleanField(default=False, verbose_name='Статус отклика - отклонен')
    status_add = models.BooleanField(default=False, verbose_name='Статус отклика - принят')

    def __str__(self):
        return f'{self.user}'
