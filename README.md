# Телеграм бот
Бот предназначен для рассылки одежды по выбранным категориям. 

Пользователь может выбрать 5 категорий:
+ Верхняя одежда
+ Джинсы, блузки, юбки
+ Обувь
+ Платья
+ Аксессуары 

Также в настройках есть скрытая категория:
+ Рассылка за 300 - все товары не дороже трехсот рублей

Существует [админская панель](https://github.com/zakhar-petukhov/telegram_shop_bot/blob/35873492e38fb674a0f00f4697a8726757fd4396/main.py#L319), 
которая проверят по user_id статус и выводит новую кнопку **Количество подписчиков**, которая 
показывает число подписавшихся юзеров на бота.

## Устройство
[utils.py](https://github.com/zakhar-petukhov/telegram_shop_bot/blob/35873492e38fb674a0f00f4697a8726757fd4396/utils.py) - 
предназначен для подключения к базе данных, а также выхода из нее.

[scripts_bd.py](https://github.com/zakhar-petukhov/telegram_shop_bot/blob/35873492e38fb674a0f00f4697a8726757fd4396/scripts_bd.py) - 
файл не имеет существенного отношения к проекту, создавался с целью мониторинга подписок на категории.

[scripts_for_send_message.py](https://github.com/zakhar-petukhov/telegram_shop_bot/blob/35873492e38fb674a0f00f4697a8726757fd4396/scripts_for_send_message.py) 
перебирает в себе всех юзеров и передает их в файл [send_message.py](https://github.com/zakhar-petukhov/telegram_shop_bot/blob/35873492e38fb674a0f00f4697a8726757fd4396/send_message.py),
где происходит рассылка сообщений, а также выявление ошибок (т.е. если бота пользователь забанил, то идет пометка в базу данных).

[users_db.sql](https://github.com/zakhar-petukhov/telegram_shop_bot/blob/35873492e38fb674a0f00f4697a8726757fd4396/users_db.sql) - дамп базы
данных, чтобы залить все данные ```mysql -u USER -p < users_db.sql```

