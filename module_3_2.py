# объявляю функцию send_email
def send_email(massage, recipient, *,  # massage - текст сообщения для отправки; recipient - адрес получателя.
               sender="university.help@gmail.com"):  # sender - адрес отправителя, аргумент по умолчанию "university.help@gmail.com"
    # проверка на корректность e-mail адресов
    def is_valid_email(email):
        return ("@" in email and
                (email.endswith(".com") or
                 email.endswith(".ru") or
                 email.endswith(".net")))

    # проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    # проверка на отправителя по умолчанию
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        if is_valid_email(sender) and is_valid_email(recipient):
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmsil.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправтье задание', 'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
