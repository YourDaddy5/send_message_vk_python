from vk_api import VkApi, AuthError
from vk_api.utils import get_random_id
import vk_api
import time
import schedule
#Импорт нужных модулей
vk_session = VkApi('тут пишешь свой номер', 'тут пароль')
vk_session.auth(token_only=True)
#чтобы получить этот токен заходишь на сайт vkhost.github.io,выбираешь Kate Mobile,даёшь все разрешения,смотришь в адрессную строку и там копируешь все символы от access_token= до &expires_in
token = "твой токен"
vk = vk_api.VkApi(token=token).get_api()


def msg():
    #chat_id для бесед,user_id для личных сообщений
    vk.messages.send(chat_id = 76, message='хай', random_id=0)

#эта строка делает функцию msg каждый день в 16:19(например)
schedule.every().day.at("16:19").do(msg)
while True:
    schedule.run_pending()
    time.sleep(1)

