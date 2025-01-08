import vk_api
from vk_api.utils import get_random_id

import portfolio.secret_token as secret

USER_ID = 286288768
SECRET_TOKEN = secret.SECRET_TOKEN


def send_to_vk(message: str):
    try:
        vk_session = vk_api.VkApi(token=SECRET_TOKEN)
        vk = vk_session.get_api()
        try:
            vk.messages.send(
                user_id=USER_ID, random_id=get_random_id(), message=message
            )
        except BaseException as ex:
            print(ex)
        print("Sent message to Timur")
    except Exception as e:
        print(f"Didn't send to Timur, {e}")
