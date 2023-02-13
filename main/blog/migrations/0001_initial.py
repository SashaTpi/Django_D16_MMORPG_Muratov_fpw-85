# Generated by Django 3.2.16 on 2023-01-28 13:53

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата поста')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок поста')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Сожержимое поста')),
                ('category', models.CharField(choices=[('tank', 'Танки'), ('healer', 'Хилы'), ('damage dealer', 'ДД'), ('vendor', 'Торговцы'), ('guildmaster', 'Гилдмастеры'), ('questgiver', 'Квестгиверы'), ('blacksmith', 'Кузнецы'), ('leatherworker', 'Кожевники'), ('potion maker', 'Зельевары'), ('spellmaster', 'Мастера заклинаний')], max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата отклика')),
                ('text', models.TextField(verbose_name='Содержимое отклика')),
                ('accept_status', models.BooleanField(default=False, verbose_name='Принятие отклика')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор отклика')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Пост отклика')),
            ],
            options={
                'verbose_name': 'Reply',
                'verbose_name_plural': 'Replies',
            },
        ),
    ]
