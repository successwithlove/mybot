from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time
import get_picture



token =  str(input("Введите токен"))
vk_session = vk_api.VkApi(token=token)


session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

hi = ["привет", "хоп хей", "ку", "здрасте", "здрасьте", "здравствуй", "здравствуйте", "добрый день",
     "доброе утро", "добрый вечер", "здорова", "здоров", "салют", "хай", "хелло", "хеллоу", "хелоу", "хело", "хэлло",
      "хэллоу", "хэлоу", "хэло", "хэлло", "приветствую", "хаю-хай", "хаю хай", "хаюхай", "саб", "здравия желаю",
      "хей", "хэй", "хоп-хей", "хопхей", "при", "дорова", "здрасть", "драсти", "здрасти", "халло", "здрасти мордасти",
      "здрасти-мордасти", "здрастимордасти", "ghbdtn"]


def get(vk_session, id_group, vk):
    print("1")
    try:
        print("2")
        print(id_group)
        print(vk)
        attachment = ''
        # print('До всего '+str(time.ctime(time.time())))
        max_num = vk.photos.get(owner_id=id_group, album_id='wall', count=0)['count']
        #max_num = vk_session.method('photos.get', {"owner_id" : id_group, "album_id": "wall"}["count"])
        print(max_num)
        print("3")
        # print('Смотрим время после получения количества всех картинок ' + str(time.ctime(time.time())))
        num = random.randint(1, max_num)
        print("num = " + num)
        print("4")
        # print('Время до получения пикчи ' + str(time.ctime(time.time())))
        pictures = vk.photos.get(owner_id=str(id_group), album_id='wall', count=1, offset=num)['items']
        buf = []
        for element in pictures:
            buf.append('photo' + str(id_group) + '_' + str(element['id']))
        print(buf)
        attachment = ','.join(buf)
        print(type(attachment))
        # print('Время после получения пикчи '+str(time.ctime(time.time())))
        print(attachment)
        return attachment

    except:
        return











def create_keyboard(x):
    keyboard = VkKeyboard(one_time=False)

    if x == 'тест':
        keyboard = VkKeyboard(one_time=True)

        keyboard.add_button('Белая кнопка', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Красная кнопка', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Синяя кнопка', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Привет', color=VkKeyboardColor.PRIMARY)


    elif x == 'смех':
        keyboard.add_button("хочу смешную картинку!", color=VkKeyboardColor.POSITIVE)

    elif x == 'король здесь':
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Король здесь', color=VkKeyboardColor.POSITIVE)

    elif x == 'закрыть':
        print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard

def send(vk_session, id_type, id, message=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), 'keyboard': keyboard})



def write(vk_session, id_type, id, type ):
    vk_session.method('messages.setActivity', {"user_id": id, "type": type})


#def read(vk_session):
   # vk_session.method('messages.markAsRead', {})

while True:
    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:

            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст: ' + str(event.text))
            print('Текст: ' + str(event.user_id))
            response = event.text.lower()
            #keyboard = create_keyboard()

            if event.from_user and not (event.from_me):
                uid = event.user_id

                if response == "король здесь" and event.user_id == idus: # idпользователя:
                    send(vk_session, "user_id", event.user_id, message="Приветствую вас, ваше величество!", keyboard=None)
                    break

                if hi.count(response) == True:

                    #read(vk_session)
                    write(vk_session, "user_id", uid,  "typing")
                    time.sleep(5)

                    send(vk_session, "user_id", uid, message='привет привет!', keyboard=create_keyboard("король здесь"))
                    write(vk_session, "user_id", uid, "typing")
                    time.sleep(5)

                    send(vk_session, "user_id", uid, message='всегда приятно беседовать с воспитанным человеком.', keyboard=None)



                if response == "тест":
                    send(vk_session, "user_id", event.user_id, message='Тестовые команды', keyboard=None)
                if response == "хочу смешную картинку!":

                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'лови скорей!',
                                                        'random_id': random.randint(-2147483648, +2147483648),
                                                        "attachment": None})




