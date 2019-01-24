import telebot
import config
from scripts_for_send_message import Script_work_with_database
import time
import utils

token = config.token
bot = telebot.TeleBot(token)


class Send_message:
    db = utils.DB(host=" ", user=" ", password=" ", db=" ")

    def __init__(self):
        self.q = Script_work_with_database()

    ###############__ Всем пользователям___######################

    def send_all_users(self, message):
        for user_id in self.q.all_users():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    ###############__ Проверка работы__######################
    def check_of_work(self):
        try:
            with self.db as cursor:
                bot.send_message(594400511, text='Проверка связи')
                cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(594400511))
        except Exception as e:
            print(e)
            if 'bot was blocked by the user' in str(e):
                with self.db as cursor:
                    cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(594400511))

    ###############__ Все категории__######################

    # Для отпраки всех категорий
    def send_message_all_category(self, message):
        for user_id in self.q.mailing_to_all_categories():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    ###############__ Одна категория__######################

    # Для отправки одной категории Одежда
    def send_message_one_category_clothes(self, message):
        for user_id in self.q.one_category_clothes():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки одной категории Обувь
    def send_message_one_category_shoes(self, message):
        for user_id in self.q.one_category_shoes():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки одной категории Платья
    def send_message_one_category_dress(self, message):
        for user_id in self.q.one_category_dress():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки одной категории Аксессуары
    def send_message_one_category_accessories(self, message):
        for user_id in self.q.one_category_accessories():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки одной категории Джинсы, блузки, юбки
    def send_message_one_category_jeans_blouses_skirts(self, message):
        for user_id in self.q.one_category_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    ###############__ Две категории__######################

    # Для отправки двух категорий Одежда, Обувь
    def send_message_two_category_clothes_and_shoes(self, message):
        for user_id in self.q.two_category_clothes_and_shoes():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки двух категорий Одежда и Платья
    def send_message_two_category_clothes_and_dress(self, message):
        for user_id in self.q.two_category_clothes_and_dress():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки двух категорий Одежда и Аксуссуары
    def send_message_two_category_clothes_and_accessories(self, message):
        for user_id in self.q.two_category_clothes_and_accessories():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки двух категорий Одежда и Джинсы, блузки, юбки
    def send_message_two_category_clothes_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.two_category_clothes_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки двух категорий Обувь и Платья
    def send_message_two_category_shoes_and_dress(self, message):
        for user_id in self.q.two_category_shoes_and_dress():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки двух категорий Обувь и Аксессуары
    def send_message_two_category_shoes_and_accessories(self, message):
        for user_id in self.q.two_category_shoes_and_accessories():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки двух категорий Обувь и Джинсы, блузки, юбки
    def send_message_two_category_shoes_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.two_category_shoes_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки двух категорий Платья и Аксессуары
    def send_message_two_category_dress_and_accessories(self, message):
        for user_id in self.q.two_category_dress_and_accessories():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки двух категорий Платья и Джинсы, блузки, юбки
    def send_message_two_category_dress_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.two_category_dress_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки двух категорий Аксессуары и Джинсы, блузки, юбки
    def send_message_two_category_accessories_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.two_category_accessories_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    ###############__ Три категории__###################

    # Для отправки трех категорий Одежда, Обувь, Платья
    def send_message_three_category_clothes_and_shoes_and_dress(self, message):
        for user_id in self.q.three_category_clothes_and_shoes_and_dress():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки трех категорий Одежда, Обувь, Аксессуары
    def send_message_three_category_clothes_and_shoes_and_accessories(self, message):
        for user_id in self.q.three_category_clothes_and_shoes_and_accessories():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки трех категорий Одежда, Обувь, Джинсы, блузки, юбки
    def send_message_three_category_clothes_and_shoes_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.three_category_clothes_and_shoes_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки трех категорий Одежда, Платья, Аксессуары
    def send_message_three_category_clothes_and_dress_and_accessories(self, message):
        for user_id in self.q.three_category_clothes_and_dress_and_accessories():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки трех категорий Одежда, Платья, Джинсы, блузки, юбки
    def send_message_three_category_clothes_and_dress_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.three_category_clothes_and_dress_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки трех категорий Одежда, Аксессуары, Джинсы, блузки, юбки
    def send_message_three_category_clothes_and_accessories_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.three_category_clothes_and_accessories_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки трех категорий Обувь, Платья, Аксессуары
    def send_message_three_category_shoes_and_dress_and_accessories(self, message):
        for user_id in self.q.three_category_shoes_and_dress_and_accessories():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки трех категорий Обувь, Платья, Джинсы, блузки, юбки
    def send_message_three_category_shoes_and_dress_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.three_category_shoes_and_dress_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки трех категорий Обувь, Аксессуары, Джинсы, блузки, юбки
    def send_message_three_category_shoes_and_accessories_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.three_category_shoes_and_accessories_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки трех категорий Платья, Аксессуары, Джинсы, блузки, юбки
    def send_message_three_category_dress_and_accessories_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.three_category_dress_and_accessories_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    ###############__ Четыре категории__###################

    # Для отправки четырех категорий Одежда, Обувь, Платья, Аксессуары
    def send_message_fourth_category_clothes_and_shoes_and_dress_and_accessories(self, message):
        for user_id in self.q.fourth_category_clothes_and_shoes_and_dress_and_accessories():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки четырех категорий Одежда, Обувь, Платья, Джинсы, блузки, юбки
    def send_message_fourth_category_clothes_and_shoes_and_dress_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.fourth_category_clothes_and_shoes_and_dress_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки четырех категорий Одежда, Обувь, Аксессуары, Джинсы, блузки, юбки
    def send_message_fourth_category_clothes_and_shoes_and_accessories_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.fourth_category_clothes_and_shoes_and_accessories_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки четырех категорий Одежда, Платья, Аксессуары, Джинсы, блузки, юбки
    def send_message_fourth_category_clothes_and_dress_and_accessories_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.fourth_category_clothes_and_dress_and_accessories_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки четырех категорий Обувь, Платья, Аксессуары, Джинсы, блузки, юбки
    def send_message_fourth_category_shoes_and_dress_and_accessories_and_jeans_blouses_skirts(self, message):
        for user_id in self.q.fourth_category_shoes_and_dress_and_accessories_and_jeans_blouses_skirts():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE table_shop SET `Бан`='Нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE table_shop SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    # Для отправки категории Рассылка за 300
    def send_message_three_hungred(self, message):
        for user_id in self.q.three_hundred():
            try:
                with self.db as cursor:
                    bot.send_message(user_id, text=message, parse_mode='markdown', disable_web_page_preview=True)
                    cursor.execute("UPDATE three_hundred SET `Бан`='нет' WHERE user_id='{}' ".format(user_id))
                    time.sleep(0.3)
            except Exception as e:
                print(e)
                if 'bot was blocked by the user' in str(e):
                    with self.db as cursor:
                        cursor.execute("UPDATE three_hundred SET `Бан`='Да' WHERE user_id='{}' ".format(user_id))

    def blocked_the_bot(self):
        with self.db as cursor:
            sum = 0
            cursor.execute("SELECT * FROM table_shop WHERE `Остановка бота`='Запущен' and `Бан`='Нет'")
            for i in cursor.fetchall():
                sum += 1
            return 'Активные пользователи = {}'.format(sum)


message = """
*Ежедневная подборка по вашим категориям:*

➖ *Футболка Tommy Jeans* 
*-45%* |⚽️| 1317₽ 👉 695₽ 📷 [Фото](https://t.me/shmotshmot/1122)
🔥 Купить — http://fas.st/imcgr

➖ *Синий вязаный джемпер* "ALCOTT"
*-54%* |⚽️| 1990₽ 👉 995₽ 📷 [Фото](https://t.me/shmotshmot/1120)
🔥 Купить — https://clck.ru/EMZHE

➖ *Свитшот с кроликом* 
*-9%* |⚽️| 740₽ 👉 670₽ 📷 [Фото](https://t.me/shmotshmot/1123)
🔥 Купить — https://clck.ru/ETgVU

➖ *Черная блуза в горошек* 
*-0%* |💎| 👉 559₽ 📷 [Фото](https://t.me/shmotshmot/494)
🔥 Купить — https://clck.ru/EMxkz

➖ *Блуза c принтом*
*-25%* |⚽️| 1599₽ 👉 1199₽ 📷 [Фото](https://t.me/shmotshmot/1128)
🔥 Купить — https://clck.ru/ETgc8

➖ *Джинсы*
*-45%* |💎| 2128₽ 👉 1170₽ 📷 [Фото](https://t.me/shmotshmot/487)
🔥 Купить — http://ali.pub/2rafcx

➖ *Ботильоны* "Hung Yau"
*-10%* |💎| 1134₽ 👉 1020₽ 📷 [Фото](https://t.me/shmotshmot/1101)
🔥 Купить — http://ali.pub/2s4oq1

➖ *Туфли на платформе*
*-28* |💎| 1469₽ 👉 1058₽ 📷 [Фото](https://t.me/shmotshmot/1102)
🔥 Купить — http://ali.pub/2s4oye

➖ *Оксфорды* "OUKAHUI"
*-30%* |💎| 1480₽ 👉 1036₽ 📷 [Фото](https://t.me/shmotshmot/1104)
🔥 Купить — http://ali.pub/2s4pbf

➖ *Платья с сочетанием контрастных цветов*
*-50%* |⚽️| 1342₽ 👉 658₽ 📷 [Фото](https://t.me/shmotshmot/1115)
🔥 Купить — http://fas.st/76aBA

➖ *Черное винтажное платье с горошкем* 
*-48%* |💎| 1743₽ 👉 906₽ 📷 [Фото](https://t.me/shmotshmot/1113)
🔥 Купить — http://ali.pub/2s4r8g

➖ *Асимметрично платья спошного цвета с короткыми рукавами*
*-45%* |⚽️| 1251₽ 👉 717₽ 📷 [Фото](https://t.me/shmotshmot/1119)
🔥 Купить — https://clck.ru/ETgFP

➖ *Палантин* "Befree"
*-40%* |💎| 799₽ 👉 444₽ 📷 [Фото](https://t.me/shmotshmot/1129)
🔥 Купить — https://f.gdeslon.ru/f/cf9e9430e3470270

➖ *Бейсболка* "True Spin"
*-60%* |💎| 899₽ 👉 402₽ 📷 [Фото](https://t.me/shmotshmot/1130)
🔥 Купить — https://f.gdeslon.ru/f/0cb2e4d0fdedc559

➖ *Клатч* "Dorothy Perkins" 
*-50%* |💎| 999₽ 👉 512₽ 📷 [Фото](https://t.me/shmotshmot/1131)
🔥 Купить — https://f.gdeslon.ru/f/c8b403097a1393ec

💎 - бесплатная доставка
⚽️ - доставка в районе 200 - 400р
📷 - фотография товара и все размеры
    
"""

send_msg = Send_message()

###############__ Проверка работы__######################
# send_msg.check_of_work()


###############__ Все категории__######################
# Для отпраки всех категорий
# send_msg.send_message_all_category(message)

###############__ Одна категория__######################
# Для отправки одной категории Одежда
# send_msg.send_message_one_category_clothes(message)

# Для отправки одной категории Обувь
# send_msg.send_message_one_category_shoes(message)

# Для отправки одной категории Платья
# send_msg.send_message_one_category_dress(message)

# Для отправки одной категории Аксессуары
# send_msg.send_message_one_category_accessories(message)

# Для отправки одной категории Джинсы, блузки, юбки
# send_msg.send_message_one_category_jeans_blouses_skirts(message)


###############__ Две категории__######################

# Для отправки двух категорий Одежда, Обувь
# send_msg.send_message_two_category_clothes_and_shoes(message)

# Для отправки двух категорий Одежда и Платья
# send_msg.send_message_two_category_clothes_and_dress(message)

# Для отправки двух категорий Одежда и Аксуссуары
# send_msg.send_message_two_category_clothes_and_accessories(message)

# Для отправки двух категорий Одежда и Джинсы, блузки, юбки
# send_msg.send_message_two_category_clothes_and_jeans_blouses_skirts(message)

# Для отправки двух категорий Обувь и Платья
# send_msg.send_message_two_category_shoes_and_dress(message)

# Для отправки двух категорий Обувь и Аксессуары
# send_msg.send_message_two_category_shoes_and_accessories(message)

# Для отправки двух категорий Обувь и Джинсы, блузки, юбки
# send_msg.send_message_two_category_shoes_and_jeans_blouses_skirts(message)

# Для отправки двух категорий Платья и Аксессуары
# send_msg.send_message_two_category_dress_and_accessories(message)

# Для отправки двух категорий Платья и Джинсы, блузки, юбки
# send_msg.send_message_two_category_dress_and_jeans_blouses_skirts(message)

# Для отправки двух категорий Аксессуары и Джинсы, блузки, юбки
# send_msg.send_message_two_category_accessories_and_jeans_blouses_skirts(message)


###############__ Три категории__######################

# Для отправки трех категорий Одежда, Обувь, Платья
# send_msg.send_message_three_category_clothes_and_shoes_and_dress(message)

# Для отправки трех категорий Одежда, Обувь, Аксессуары
# send_msg.send_message_three_category_clothes_and_shoes_and_accessories(message)

# Для отправки трех категорий Одежда, Обувь, Джинсы, блузки, юбки
# send_msg.send_message_three_category_clothes_and_shoes_and_jeans_blouses_skirts(message)

# Для отправки трех категорий Одежда, Платья, Аксессуары
# send_msg.send_message_three_category_clothes_and_dress_and_accessories(message)

# Подписка на три категории Одежда, Платья и Джинсы, блузки, юбки:
# send_msg.send_message_three_category_clothes_and_dress_and_jeans_blouses_skirts(message)

# Для отправки трех категорий Одежда, Аксессуары, Джинсы, блузки, юбки
# send_msg.send_message_three_category_clothes_and_accessories_and_jeans_blouses_skirts(message)

# Для отправки трех категорий Обувь, Платья, Аксессуары
# send_msg.send_message_three_category_shoes_and_dress_and_accessories(message)

# Для отправки трех категорий Обувь, Платья, Джинсы, блузки, юбки
# send_msg.send_message_three_category_shoes_and_dress_and_jeans_blouses_skirts(message)

# Для отправки трех категорий Обувь, Аксессуары, Джинсы, блузки, юбки
# send_msg.send_message_three_category_shoes_and_accessories_and_jeans_blouses_skirts(message)

# Для отправки трех категорий Платья, Аксессуары, Джинсы, блузки, юбки
# send_msg.send_message_three_category_dress_and_accessories_and_jeans_blouses_skirts(message)


###############__ Четыре категории__###################

# Для отправки четырех категорий Одежда, Обувь, Платья, Аксессуары
# send_msg.send_message_fourth_category_clothes_and_shoes_and_dress_and_accessories(message)

# Для отправки четырех категорий Одежда, Обувь, Платья, Джинсы, блузки, юбки
# send_msg.send_message_fourth_category_clothes_and_shoes_and_dress_and_jeans_blouses_skirts(message)

# Для отправки четырех категорий Одежда, Обувь, Аксессуары, Джинсы, блузки, юбки
# send_msg.send_message_fourth_category_clothes_and_shoes_and_accessories_and_jeans_blouses_skirts(message)

# Для отправки четырех категорий Одежда, Платья, Аксессуары, Джинсы, блузки, юбки
# send_msg.send_message_fourth_category_clothes_and_dress_and_accessories_and_jeans_blouses_skirts(message)

# Для отправки четырех категорий Обувь, Платья, Аксессуары, Джинсы, блузки, юбки
# send_msg.send_message_fourth_category_shoes_and_dress_and_accessories_and_jeans_blouses_skirts(message)


###############__ Всем пользователям___######################

# Для отправки обновлений для всех юзеров
# send_msg.send_all_users(message)

###############__ Категория за 300___######################

# Для отправки категории за 300
# send_msg.send_message_three_hungred(message)

###############__ Проверка кто заблокировал бота___######################

# print(send_msg.blocked_the_bot())














