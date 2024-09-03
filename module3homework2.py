def send_email(message, recepient, sender = "university.help@gmail.com"):
    if not (
        "@" in sender and
        "@" in recepient and
        sender.endswith((".com",".ru",".net")) and
        recepient.endswith((".com",".ru",".net"))):
            output = f'Невозможно отправить письмо с адреса {sender} на адрес {recepient}'
    elif sender == recepient:
        output = "Нельзя отправить письмо самому себе!"
    elif sender == "university.help@gmail.com":
        output = f'Письмо успешно отправлено с адреса {sender} на адрес {recepient}.'
    else:
        output = f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recepient}.'
    print(output)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')