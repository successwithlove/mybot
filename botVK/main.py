from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time



token = str(input("Введите токен"))
vk_session = vk_api.VkApi(token=token)


session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

hi = ["привет", "приве", "хоп хей", "ку", "здрасте", "здрасьте", "здравствуй", "здравствуйте", "добрый день",
     "доброе утро", "добрый вечер", "здорова", "здоров", "салют", "хай"]

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст: ' + str(event.text))
            print('Текст: ' + str(event.user_id))
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if hi.count(response) == True:
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Привет привет!', 'random_id': 0})
                if response == "король здесь" and event.user_id == idпользователя:
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Приветствую вас, ваше величество!', 'random_id': 0})
