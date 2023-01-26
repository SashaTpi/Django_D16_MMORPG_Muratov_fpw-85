from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Response, Note


@receiver(post_save, sender=Response)
def send_msg(instance, created, **kwargs):
    user = User.objects.get(pk=instance.user_response_id)
    pk_pesponse = instance.id
    if created:

        pk_note = instance.note_id
        user = f'{user.first_name} {user.last_name}'
        user_id = Note.objects.get(pk=pk_note).user_id
        note_title = Note.objects.get(pk=pk_note).title
        response_content = Response.objects.get(pk=pk_pesponse).content
        response_time = Response.objects.get(pk=pk_pesponse).datetime


        title = f'У вас новый отклик от {str(user)[:15]}'
        msg = f'На ваше объявление "{note_title}" пришел {str(response_time)[:19]} новый отклик\n' \
              f'от {user} следующего содержания: ' \
              f'{response_content}. Перейти в отклики http://127.0.0.1:8000/response/'
        email = 'testpostnoname@yandex.ru'
        note_email = User.objects.get(pk=user_id).email

        send_mail(subject=title, message=msg, from_email=email, recipient_list=[note_email, ])

        print("\n*************** ВЫВОД ПИСЬМА В КОНСОЛЬ (для удобства тестирования почты) *********************\n")
        print('Тема письма:', title)
        print('Контент письма:', msg)
        print('Адрес почты сервера:', email)
        print('Адрес отправления:', note_email)
        print("\n************************************ КОНЕЦ ПИСЬМА ********************************************\n")

    elif instance.status_add:

        note_title = Note.objects.get(pk=Response.objects.get(pk=pk_pesponse).note_id).title
        note_id = Note.objects.get(pk=Response.objects.get(pk=pk_pesponse).note_id).id
        response_time = Response.objects.get(pk=pk_pesponse).datetime

        title = f'У вас одобренный отклик на объявление "{str(note_title)[:15]}"'
        msg = f'На ваш отклик от {str(response_time)[:19]} на объявление "{note_title}" пришло положительное ' \
              f'подтверждение. Перейти на объявление http://127.0.0.1:8000/detail/{note_id}'
        email = 'testpostnoname@yandex.ru'
        response_email = User.objects.get(pk=Response.objects.get(pk=pk_pesponse).user_response_id).email

        send_mail(subject=title, message=msg, from_email=email, recipient_list=[response_email, ])

        print("\n*************** ВЫВОД ПИСЬМА В КОНСОЛЬ (для удобства тестирования почты) **********************\n")
        print('Тема письма:', title)
        print('Контент письма:', msg)
        print('Адрес почты сервера:', email)
        print('Адрес отправления:', response_email)
        print("\n************************************ КОНЕЦ ПИСЬМА ********************************************\n")
