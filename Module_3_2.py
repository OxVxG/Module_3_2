# Решение №1(свое)

def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса: ", sender, "на адрес: ", recipient)
    elif ("@" and (".com" or ".ru" or ".net")) not in (recipient and sender):
        print("Невозможно отправить письмо с адреса: ", sender, "на адрес: ", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса: ", sender, "на адрес: ", recipient)

# # Решение №2 (подсмотрено, понравилось .find и .endswith!)
# def send_email(message, recipient, *, sender = "university.help@gmail.com"):
#     boole = recipient.find('@') >= 0 and recipient.endswith((".com", ".ru", ".net")) \
#             and sender.find('@') >= 0 and sender.endswith((".com", ".ru", ".net"))
#     if boole == False:
#         print("Невозможно отправить письмо с адреса: ", sender, "на адрес: ", recipient)
#         return
#     if recipient == sender:
#         print("Нельзя отправить письмо самому себе!")
#         return
#     if sender == "university.help@gmail.com":
#         print("Письмо успешно отправлено с адреса: ", sender, "на адрес: ", recipient)
#     else:
#         print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса: ", sender, "на адрес: ", recipient)

# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')                                                #Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')   #НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')                  #Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')               # Нельзя отправить письмо самому себе!