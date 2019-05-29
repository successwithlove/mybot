from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time


token = str(input("Введите токен"))
vk_session = vk_api.VkApi(token=token)


session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст: ' + str(event.text))
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Привет привет!', 'random_id': 0})
