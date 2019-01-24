import cherrypy
import telebot

import config
import utils

token = config.token
bot = telebot.TeleBot(token)

WEBHOOK_HOST = ' '
WEBHOOK_PORT = 443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = './webhook_cert.pem'
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % config.token

DEPARTURE_LANDING_DATA_FOR_PARSER = {}
DEPARTURE_LANDING_DATA_FOR_USER = {}


class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                'content-type' in cherrypy.request.headers and \
                cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


class Update_bd_three_hundred:
    db = utils.DB(host=" ", user=" ", password=" ", db=" ")

    def verification_id_three_hundred(self, cursor):
        cursor.execute("SELECT user_id FROM three_hundred")
        return [x[0] for x in cursor.fetchall()]

    def update_bd_for_user_id_three_hundred(self, user_id):
        with self.db as cursor:
            if user_id not in self.verification_id_three_hundred(cursor):
                cursor.execute("INSERT INTO three_hundred VALUES(%s,%s,%s)", (user_id, 'Нет', 'нет'))

    def start_dispatch(self, user_id):
        with self.db as cursor:
            cursor.execute("SELECT * FROM three_hundred WHERE user_id='{}' ".format(user_id))
            return cursor.fetchall()

    def add_subscription(self, user_id, chat_id, message_id):
        with self.db as cursor:
            cursor.execute("UPDATE three_hundred SET `Подписка`='Да' WHERE user_id='{}' ".format(user_id))
            user_markup = telebot.types.InlineKeyboardMarkup(True)
            subscribe_button = telebot.types.InlineKeyboardButton(text='Отписаться от рассылки',
                                                                  callback_data='Отписаться от рассылки')
            back_button = telebot.types.InlineKeyboardButton(text='Назад', callback_data='Назад')
            user_markup.add(subscribe_button, back_button)
            bot.edit_message_text(chat_id=chat_id, text="""Это рассылка аксессуаров, обуви и вообще любой одежды *не \
дороже 300₽.* Она работает *независимо* от основной подборки и выходит не каждый день. Обычно днем.

Жми *"Подписаться на рассылку"*, чтобы получать товары не дороже трех соток!""", message_id=message_id,
                                  parse_mode='markdown', reply_markup=user_markup)

    def delete_subscription(self, user_id, chat_id, message_id):
        with self.db as cursor:
            cursor.execute("UPDATE three_hundred SET `Подписка`='Нет' WHERE user_id='{}' ".format(user_id))
            user_markup = telebot.types.InlineKeyboardMarkup(True)
            subscribe_button = telebot.types.InlineKeyboardButton(text='Подписаться на рассылку',
                                                                  callback_data='Подписаться на рассылку')
            back_button = telebot.types.InlineKeyboardButton(text='Назад', callback_data='Назад')
            user_markup.add(subscribe_button, back_button)
            bot.edit_message_text(chat_id=chat_id, text="""Это рассылка аксессуаров, обуви и вообще любой одежды *не \
дороже 300₽.* Она работает *независимо* от основной подборки и выходит не каждый день. Обычно днем.

Жми *"Подписаться на рассылку"*, чтобы получать товары не дороже трех соток!""", message_id=message_id,
                                  parse_mode='markdown', reply_markup=user_markup)

    def back(self, user_id, chat_id, message_id):
        update_bd = Update_bd()
        for i in update_bd.check_start_bot(user_id):
            if 'Остановлен' in i:
                user_markup = telebot.types.InlineKeyboardMarkup(True)
                setting_categories_button = telebot.types.InlineKeyboardButton(text='Категории',
                                                                               callback_data='Настройка категорий')
                three_hundred = telebot.types.InlineKeyboardButton(text='Рассылка за 300',
                                                                   callback_data='Рассылка за 300')
                start_bot_button = telebot.types.InlineKeyboardButton(text='Возобновить бота',
                                                                      callback_data='Возобновить бота')
                user_markup.add(setting_categories_button, three_hundred, start_bot_button)
                bot.edit_message_text(text='Если что-то непонятно — жми *"О боте"*', chat_id=chat_id,
                                      message_id=message_id, parse_mode='markdown', reply_markup=user_markup)
            else:
                user_markup = telebot.types.InlineKeyboardMarkup(True)
                setting_categories_button = telebot.types.InlineKeyboardButton(text='Категории',
                                                                               callback_data='Настройка категорий')
                three_hundred = telebot.types.InlineKeyboardButton(text='Рассылка за 300',
                                                                   callback_data='Рассылка за 300')
                stop_bot_button = telebot.types.InlineKeyboardButton(text='Приостановить бота',
                                                                     callback_data='Приостановить бота')
                user_markup.add(setting_categories_button, three_hundred, stop_bot_button)
                bot.edit_message_text(text='Если что-то непонятно — жми *"О боте"*', chat_id=chat_id,
                                      message_id=message_id, parse_mode='markdown', reply_markup=user_markup)

    def unloading_from_the_database(self):
        with self.db as cursor:
            sum = 0
            cursor.execute("SELECT * FROM three_hundred WHERE `Подписка`='Да' and `Бан`='нет' ")
            for i in cursor.fetchall():
                sum += 1
            return sum


class Update_bd:
    db = utils.DB(host=" ", user=" ", password=" ", db=" ")

    def verification_id(self, cursor):
        cursor.execute("SELECT user_id FROM table_shop")
        return [x[0] for x in cursor.fetchall()]

    def update_bd_for_user_id(self, user_id):
        with self.db as cursor:
            if user_id not in self.verification_id(cursor):
                cursor.execute("INSERT INTO table_shop VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                               (user_id, 'удалено Верхняя одежда', 'удалено Джинсы, блузки, юбки',
                                'удалено Обувь', 'удалено Платья', 'удалено Аксессуары', 'Запущен', 'Нет'))

    def start_delete_category(self, user_id, chat_id, message_id, cursor):
        cursor.execute("SELECT * FROM table_shop WHERE user_id='{}' ".format(user_id))
        check_db = cursor.fetchall()[0][1:-2]
        user_markup = telebot.types.InlineKeyboardMarkup(True)
        ready_button = telebot.types.InlineKeyboardButton(text='Готово 👍', callback_data='Готово')
        category_button = ['Верхняя одежда', 'Джинсы, блузки, юбки', 'Обувь', 'Платья', 'Аксессуары']
        actual_button = []
        for i in category_button:
            if i not in check_db:
                actual_button.append(i)
        user_markup.add(*[telebot.types.InlineKeyboardButton(text=name, callback_data=name)
                          for name in actual_button], ready_button)
        bot.edit_message_text(chat_id=chat_id, text='Какие категории товаров будет присылать бот?🤔',
                              message_id=message_id, reply_markup=user_markup)

    def update_bd_for_outerwear(self, user_id, chat_id, message_id, button_data):
        with self.db as cursor:
            cursor.execute("UPDATE table_shop SET `Верхняя одежда`='Верхняя одежда' \
            WHERE user_id='{}' ".format(user_id))
            if button_data != 'Верхняя одежда (добавить)':
                self.start_delete_category(user_id, chat_id, message_id, cursor)

    def update_bd_for_jeans_blouses_skirts(self, user_id, chat_id, message_id, button_data):
        with self.db as cursor:
            cursor.execute("UPDATE table_shop SET `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' \
            WHERE user_id='{}' ".format(user_id))
            if button_data != 'Джинсы, блузки, юбки (добавить)':
                self.start_delete_category(user_id, chat_id, message_id, cursor)

    def update_bd_for_shoes(self, user_id, chat_id, message_id, button_data):
        with self.db as cursor:
            cursor.execute("UPDATE table_shop SET `Обувь`='Обувь' WHERE user_id='{}' ".format(user_id))
            if button_data != 'Обувь (добавить)':
                self.start_delete_category(user_id, chat_id, message_id, cursor)

    def update_bd_for_dress(self, user_id, chat_id, message_id, button_data):
        with self.db as cursor:
            cursor.execute("UPDATE table_shop SET `Платья`='Платья' WHERE user_id='{}' ".format(user_id))
            if button_data != 'Платья (добавить)':
                self.start_delete_category(user_id, chat_id, message_id, cursor)

    def update_bd_for_accessories(self, user_id, chat_id, message_id, button_data):
        with self.db as cursor:
            cursor.execute("UPDATE table_shop SET `Аксессуары`='Аксессуары' WHERE user_id='{}' ".format(user_id))
            if button_data != 'Аксессуары (добавить)':
                self.start_delete_category(user_id, chat_id, message_id, cursor)

    def actual_dispatch(self, user_id):
        with self.db as cursor:
            unloading = []
            cursor.execute("SELECT * FROM table_shop WHERE user_id='{}' ".format(user_id))
            check_db = cursor.fetchall()[0][1:-2]
            for i in check_db:
                if 'удалено' not in i:
                    unloading.append(i)
            return unloading

    def delete_outerwear(self, user_id):
        with self.db as cursor:
            cursor.execute("UPDATE table_shop SET `Верхняя одежда`='удалено Верхняя одежда' \
            WHERE user_id='{}' ".format(user_id))

    def delete_jeans_blouses_skirts(self, user_id):
        with self.db as cursor:
            cursor.execute("UPDATE table_shop SET `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' WHERE \
            user_id='{}' ".format(user_id))

    def delete_shoes(self, user_id):
        with self.db as cursor:
            cursor.execute("UPDATE table_shop SET `Обувь`='удалено Обувь' WHERE user_id='{}' ".format(user_id))

    def delete_dress(self, user_id):
        with self.db as cursor:
            cursor.execute("UPDATE table_shop SET `Платья`='удалено Платья' WHERE user_id='{}' ".format(user_id))

    def delete_accessories(self, user_id):
        with self.db as cursor:
            cursor.execute("UPDATE table_shop SET `Аксессуары`='удалено Аксессуары' WHERE user_id='{}' ".format(
                user_id))

    def deleting_category(self, user_id, chat_id, message_id):
        user_markup = telebot.types.InlineKeyboardMarkup(True)

        if len(self.actual_dispatch(user_id)) < 5:
            add_category_button = telebot.types.InlineKeyboardButton(text='Добавить категорию ✅',
                                                                     callback_data='Добавить категорию')
            ready_button = telebot.types.InlineKeyboardButton(text='Готово 👍', callback_data='Готово')
            back_button = telebot.types.InlineKeyboardButton(text='Назад', callback_data='Назад')
            user_markup.add(*[telebot.types.InlineKeyboardButton(text=name + ' (удалить)',
                                                                 callback_data=name + ' (удалить)')
                              for name in self.actual_dispatch(str(user_id))], add_category_button, ready_button,
                            back_button)
            bot.edit_message_text(text='Твоя подборка составляется по категориям:', chat_id=chat_id,
                                  message_id=message_id, reply_markup=user_markup)

        else:
            ready_button = telebot.types.InlineKeyboardButton(text='Готово 👍', callback_data='Готово')
            back_button = telebot.types.InlineKeyboardButton(text='Назад', callback_data='Назад')
            user_markup.add(*[telebot.types.InlineKeyboardButton(text=name + ' (удалить)',
                                                                 callback_data=name + ' (удалить)')
                              for name in self.actual_dispatch(str(user_id))], ready_button, back_button)
            bot.edit_message_text(text='Твоя подборка составляется по категориям:', chat_id=chat_id,
                                  message_id=message_id, reply_markup=user_markup)

    def add_category(self, user_id):
        with self.db as cursor:
            unloading = []
            cursor.execute("SELECT * FROM table_shop WHERE user_id='{}'".format(user_id))
            check_db = cursor.fetchall()[0][1:-2]
            for i in check_db:
                if 'удалено' in i:
                    unloading.append(i.replace('удалено ', ''))
            return unloading

    def delete_dispatch(self, user_id, chat_id, message_id):
        if len(self.add_category(user_id)) == 0:
            self.deleting_category(user_id, chat_id, message_id)
        else:
            user_markup = telebot.types.InlineKeyboardMarkup(True)
            ready_button = telebot.types.InlineKeyboardButton(text='Готово 👍', callback_data='Готово')
            user_markup.add(*[telebot.types.InlineKeyboardButton(text=name + ' (добавить)',
                                                                 callback_data=name + ' (добавить)')
                              for name in self.add_category(str(user_id))], ready_button)
            bot.edit_message_text(text='Вы можете добавить следующие категории', chat_id=chat_id,
                                  message_id=message_id, reply_markup=user_markup)

    def stop_bot(self, user_id, chat_id, message_id):
        with self.db as cursor:
            cursor.execute("UPDATE table_shop SET `Остановка бота`='Остановлен' WHERE user_id='{}' ".format(user_id))
            user_markup = telebot.types.InlineKeyboardMarkup(True)
            setting_categories_button = telebot.types.InlineKeyboardButton(text='Категории',
                                                                           callback_data='Настройка категорий')
            start_bot_button = telebot.types.InlineKeyboardButton(text='Возобновить бота',
                                                                  callback_data='Возобновить бота')
            three_hundred = telebot.types.InlineKeyboardButton(text='Рассылка за 300',
                                                               callback_data='Рассылка за 300')
            user_markup.add(setting_categories_button, three_hundred, start_bot_button)
            bot.edit_message_text(text='Если что-то непонятно — жми *"О боте"*', chat_id=chat_id,
                                  message_id=message_id, parse_mode='markdown', reply_markup=user_markup)

    def start_bot(self, user_id, chat_id, message_id):
        with self.db as cursor:
            cursor.execute("UPDATE table_shop SET `Остановка бота`='Запущен' WHERE user_id='{}' ".format(user_id))
            user_markup = telebot.types.InlineKeyboardMarkup(True)
            setting_categories_button = telebot.types.InlineKeyboardButton(text='Категории',
                                                                           callback_data='Настройка категорий')
            stop_bot_button = telebot.types.InlineKeyboardButton(text='Приостановить бота',
                                                                 callback_data='Приостановить бота')
            three_hundred = telebot.types.InlineKeyboardButton(text='Рассылка за 300',
                                                               callback_data='Рассылка за 300')
            user_markup.add(setting_categories_button, three_hundred, stop_bot_button)
            bot.edit_message_text(text='Если что-то непонятно — жми *"О боте"*', chat_id=chat_id,
                                  message_id=message_id, parse_mode='markdown', reply_markup=user_markup)

    def check_start_bot(self, user_id):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE user_id='{}' ".format(user_id))
            return cursor.fetchall()

    def unloading_from_the_database(self):
        with self.db as cursor:
            sum = 0
            cursor.execute("SELECT * FROM table_shop WHERE `Остановка бота`='Запущен' and `Бан`='Нет'")
            for i in cursor.fetchall():
                sum += 1
            return sum

    def add_all_category(self, user_id, chat_id, message_id):
        with self.db as cursor:
            cursor.execute("UPDATE table_shop SET `Верхняя одежда`='Верхняя одежда', \
`Джинсы, блузки, юбки`='Джинсы, блузки, юбки', `Обувь`='Обувь', `Платья`='Платья', `Аксессуары`='Аксессуары' \
WHERE user_id='{}' ".format(user_id))
            bot.edit_message_text(chat_id=chat_id,
                                  text="""Готово! Бот будет присылать товары по этим категориям: \
*{}*  ·  *{}*  ·  *{}*  · *{}*  ·  *{}*

Кстати, ты всегда можешь поменять категории товаров! Для этого перейди по \
кнопкам *"Настройки"* >>> *"Категории*" """.format('Верхняя одежда', 'Джинсы, блузки, юбки',
                                                   'Обувь', 'Платья', 'Аксессуары', 'Тренды'),
                                  parse_mode='markdown', message_id=message_id)


@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if (str(user_id) == '581399359') or (str(user_id) == '135374103'):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Количество подписчиков')
        bot.send_message(chat_id, 'Приветствую, админ', reply_markup=user_markup)
    else:
        update_bd = Update_bd()
        update_bd.update_bd_for_user_id(str(user_id))
        user_markup_keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup_keyboard.row('Настройки 🛠')
        user_markup_keyboard.row('О боте', 'Поддержка')
        user_markup_inline = telebot.types.InlineKeyboardMarkup(True)
        category_button = ['Верхняя одежда', 'Джинсы, блузки, юбки', 'Обувь', 'Платья', 'Аксессуары']
        add_all = telebot.types.InlineKeyboardButton(text='Добавить все категории ✅',
                                                     callback_data='Добавить все категории')

        user_markup_inline.add(*[telebot.types.InlineKeyboardButton(text=name, callback_data=name)
                                 for name in category_button], add_all)

        bot.send_message(chat_id, """Погнали! Теперь *раз в день* (с 18:00 до 21:00 по мск) ты будешь получать \
подборку товаров с хорошим скидоном — и не дороже кальяна!""",
                         reply_markup=user_markup_keyboard, parse_mode='markdown')
        bot.send_message(chat_id, 'Какие категории товаров будет присылать бот?🤔',
                         reply_markup=user_markup_inline)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def start_handler(message):
    chat_id = message.chat.id
    text = message.text
    user_id = message.from_user.id
    update_bd = Update_bd()
    update_db_for_three_hundred = Update_bd_three_hundred()
    if text == 'Настройки 🛠':
        for i in update_bd.check_start_bot(user_id):
            if 'Остановлен' in i:
                user_markup = telebot.types.InlineKeyboardMarkup(True)
                setting_categories_button = telebot.types.InlineKeyboardButton(text='Категории',
                                                                               callback_data='Настройка категорий')
                three_hundred = telebot.types.InlineKeyboardButton(text='Рассылка за 300',
                                                                   callback_data='Рассылка за 300')
                start_bot_button = telebot.types.InlineKeyboardButton(text='Возобновить бота',
                                                                      callback_data='Возобновить бота')
                user_markup.add(setting_categories_button, three_hundred, start_bot_button)
                bot.send_message(chat_id, 'Если что-то непонятно — жми *"О боте"*', parse_mode='markdown',
                                 reply_markup=user_markup)
            else:
                user_markup = telebot.types.InlineKeyboardMarkup(True)
                setting_categories_button = telebot.types.InlineKeyboardButton(text='Категории',
                                                                               callback_data='Настройка категорий')
                three_hundred = telebot.types.InlineKeyboardButton(text='Рассылка за 300',
                                                                   callback_data='Рассылка за 300')
                stop_bot_button = telebot.types.InlineKeyboardButton(text='Приостановить бота',
                                                                     callback_data='Приостановить бота')
                user_markup.add(setting_categories_button, three_hundred, stop_bot_button)
                bot.send_message(chat_id, 'Если что-то непонятно — жми *"О боте"*', parse_mode='markdown',
                                 reply_markup=user_markup)

    if text == 'О боте':
        bot.send_message(chat_id, """
*— Зачем вообще нужен ваш бот?*

👉 Чтобы экономить время и деньги. Интернет-магазины часто устраивают акции и скидки, но мы не узнаем про них, потому \
    что нет единого способа получать сразу все предложения. И бот идеально подходит для этой задачи.

*— Что он умеет делать?*

👉 Бот присылает товары по пяти категориям: верхняя одежда | джинсы, блузки, юбки | обувь | платья | аксессуары. Можно \
подписаться только на обувь, а можно выбрать все — решать тебе :)

*— Что значит «не дороже кальяна»?*

👉 Кальян — это просто удобный индекс. Как бигмак. Четкого ограничения по цене нет, но если приблизительно, то в \
районе ~1200-1300₽. Это значит, что мы не упустим классные джинсы за 1305₽!😎

*— Как часто бот присылает подборку товаров?*

👉 Раз в день с 18:00 до 21:00 по мск. 

*— И сколько товаров в одной рассылке?*

👉 Всего 8-12. При этом неважно, сколько выбрано категорий — одна или пять. 

*— Больше не хочу получать товары по обуви, теперь мне нужны платья! Как исправить?*

👉 Легко. Кликай по кнопкам *"Настройки"* > *"Категории"* и выбирай нужные. 

*— Какие товары присылает бот в категории "Верхняя одежда"?*

👉 Куртки, пальто, джемперы, жилеты, плащи, парки, накидки, футболки, майки, водолазки. 

*— Мне нравится бот, но я хочу ненадолго приостановить его. Так можно?*

👉 Конечно. Снова заходи в *"Настройки"* >>> *"Приостановить бота"*. Он заработает тогда, когда ты захочешь \
(для этого жми *"Настройки"* >>> *"Возобновить бота"*).

*— Что-то еще?*

👉 Да. Если ты читаешь это — у нас для тебя секрет. Только тсс! Если кликнуть по кнопкам *"Настройки"* >>> *"Рассылка \
за 300"*, то найдешь нашу вторую рассылку. 

Она работает независимо от первой и выходит не каждый день. Если подписаться, то бот будет присылать аксессуары, \
обувь и вообще любую одежду не дороже 300₽!

*— У меня есть вопрос/предложение! Как с вами связаться?*

👉 В меню есть кнопка *"Поддержка"*. Но на всякий случай продублируем и здесь: @SupHookaShmotBot""",
                         parse_mode='markdown')

    if text == 'Поддержка':
        bot.send_message(chat_id, """
Если бот нестабильно работает или цена на сайте отличается от той, что мы прислали, \
то стоит написать сюда: @SupHookaShmotBot""")

    if text == 'Количество подписчиков':
        if (str(user_id) == '581399359') or (str(user_id) == '135374103'):
            msg_stand = update_bd.unloading_from_the_database()
            msg_for_thee = update_db_for_three_hundred.unloading_from_the_database()
            bot.send_message(chat_id, """Юзеров подписавшихся на *стандартную* рассылку: *{}*

Юзеров подписавшихся на рассылку *за 300:* *{}*""".format(msg_stand, msg_for_thee), parse_mode='markdown')


@bot.callback_query_handler(func=lambda button: True)
def selection_of_buttons(button):
    chat_id = button.message.chat.id
    user_id = button.from_user.id
    message_id = button.message.message_id
    update_db = Update_bd()

    if button.data == 'Верхняя одежда':
        bot.answer_callback_query(button.id, text="Верхняя одежда выбрана")
        update_db.update_bd_for_outerwear(str(user_id), chat_id, message_id, button.data)

    if button.data == 'Обувь':
        bot.answer_callback_query(button.id, text="Обувь выбрана")
        update_db.update_bd_for_shoes(str(user_id), chat_id, message_id, button.data)

    if button.data == 'Платья':
        bot.answer_callback_query(button.id, text="Платья выбраны")
        update_db.update_bd_for_dress(str(user_id), chat_id, message_id, button.data)

    if button.data == 'Аксессуары':
        bot.answer_callback_query(button.id, text="Аксессуары выбраны")
        update_db.update_bd_for_accessories(str(user_id), chat_id, message_id, button.data)

    if button.data == 'Джинсы, блузки, юбки':
        bot.answer_callback_query(button.id, text="Джинсы, блузки, юбки выбраны")
        update_db.update_bd_for_jeans_blouses_skirts(str(user_id), chat_id, message_id, button.data)

    if button.data == 'Готово':
        if not update_db.actual_dispatch(user_id):
            user_markup = telebot.types.InlineKeyboardMarkup(True)
            add_category_button = telebot.types.InlineKeyboardButton(text='Добавить категорию ✅',
                                                                     callback_data='Добавить категорию')
            user_markup.add(add_category_button)
            bot.edit_message_text(chat_id=chat_id, text='Какие товары будет присылать бот? Выбери категории 👇',
                                  message_id=message_id, reply_markup=user_markup)
        else:
            bot.edit_message_text(chat_id=chat_id,
                                  text="""Готово! Бот будет присылать товары по этим категориям: *{}* 

Кстати, ты всегда можешь поменять категории товаров! Для этого перейди по кнопкам *"Настройки"* >>> \
*"Категории"* """.format(' · '.join(update_db.actual_dispatch(user_id))), parse_mode='markdown',
                                  message_id=message_id)

    if button.data == 'Настройка категорий':
        update_db.deleting_category(user_id, chat_id, message_id)

    if button.data == 'Приостановить бота':
        update_db.stop_bot(user_id, chat_id, message_id)

    if button.data == 'Возобновить бота':
        update_db.start_bot(user_id, chat_id, message_id)

    if button.data == 'Верхняя одежда (удалить)':
        update_db.delete_outerwear(user_id)
        update_db.deleting_category(user_id, chat_id, message_id)

    if button.data == 'Обувь (удалить)':
        update_db.delete_shoes(user_id)
        update_db.deleting_category(user_id, chat_id, message_id)

    if button.data == 'Платья (удалить)':
        update_db.delete_dress(user_id)
        update_db.deleting_category(user_id, chat_id, message_id)

    if button.data == 'Аксессуары (удалить)':
        update_db.delete_accessories(user_id)
        update_db.deleting_category(user_id, chat_id, message_id)

    if button.data == 'Джинсы, блузки, юбки (удалить)':
        update_db.delete_jeans_blouses_skirts(user_id)
        update_db.deleting_category(user_id, chat_id, message_id)

    if button.data == 'Добавить категорию':
        update_db.delete_dispatch(user_id, chat_id, message_id)

    if button.data == 'Верхняя одежда (добавить)':
        update_db.update_bd_for_outerwear(user_id, chat_id, message_id, button.data)
        update_db.delete_dispatch(user_id, chat_id, message_id)

    if button.data == 'Обувь (добавить)':
        update_db.update_bd_for_shoes(user_id, chat_id, message_id, button.data)
        update_db.delete_dispatch(user_id, chat_id, message_id)

    if button.data == 'Платья (добавить)':
        update_db.update_bd_for_dress(user_id, chat_id, message_id, button.data)
        update_db.delete_dispatch(user_id, chat_id, message_id)

    if button.data == 'Аксессуары (добавить)':
        update_db.update_bd_for_accessories(user_id, chat_id, message_id, button.data)
        update_db.delete_dispatch(user_id, chat_id, message_id)

    if button.data == 'Джинсы, блузки, юбки (добавить)':
        update_db.update_bd_for_jeans_blouses_skirts(user_id, chat_id, message_id, button.data)
        update_db.delete_dispatch(user_id, chat_id, message_id)

    if button.data == 'Добавить все категории':
        update_db.add_all_category(user_id, chat_id, message_id)

    if button.data == 'Рассылка за 300':
        update_bd_three_hundred = Update_bd_three_hundred()
        update_bd_three_hundred.update_bd_for_user_id_three_hundred(str(user_id))
        user_markup = telebot.types.InlineKeyboardMarkup(True)

        for i in update_bd_three_hundred.start_dispatch(str(user_id)):
            if 'Нет' in i:
                subscribe_button = telebot.types.InlineKeyboardButton(text='Подписаться на рассылку',
                                                                      callback_data='Подписаться на рассылку')
                back_button = telebot.types.InlineKeyboardButton(text='Назад', callback_data='Назад')
                user_markup.add(subscribe_button, back_button)
                bot.edit_message_text(chat_id=chat_id, text="""Это рассылка аксессуаров, обуви и вообще любой \
одежды *не дороже 300₽.* Она работает *независимо* от основной подборки и выходит не каждый день. Обычно днем.

Жми *"Подписаться на рассылку"*, чтобы получать товары не дороже трех соток!""", message_id=message_id,
                                      parse_mode='markdown', reply_markup=user_markup)
            else:
                subscribe_button = telebot.types.InlineKeyboardButton(text='Отписаться от рассылки',
                                                                      callback_data='Отписаться от рассылки')
                back_button = telebot.types.InlineKeyboardButton(text='Назад', callback_data='Назад')
                user_markup.add(subscribe_button, back_button)
                bot.edit_message_text(chat_id=chat_id, text="""Это рассылка аксессуаров, обуви и вообще любой \
одежды *не дороже 300₽.* Она работает *независимо* от основной подборки и выходит не каждый день. Обычно днем.

Жми *"Подписаться на рассылку"*, чтобы получать товары не дороже трех соток!""", message_id=message_id,
                                      parse_mode='markdown', reply_markup=user_markup)

    if button.data == 'Подписаться на рассылку':
        update_bd_three_hundred = Update_bd_three_hundred()
        update_bd_three_hundred.add_subscription(user_id, chat_id, message_id)

    if button.data == 'Отписаться от рассылки':
        update_bd_three_hundred = Update_bd_three_hundred()
        update_bd_three_hundred.delete_subscription(user_id, chat_id, message_id)

    if button.data == 'Назад':
        update_bd_three_hundred = Update_bd_three_hundred()
        update_bd_three_hundred.back(user_id, chat_id, message_id)


bot.remove_webhook()

bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})

cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})
