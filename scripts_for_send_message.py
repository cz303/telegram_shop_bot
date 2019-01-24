import pymysql
import utils


class Script_work_with_database:
    db = utils.DB(host=" ", user=" ", password=" ", db=" ")

    def all_users(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def mailing_to_all_categories(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def one_category_clothes(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def one_category_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def one_category_shoes(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def one_category_dress(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def one_category_accessories(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def two_category_clothes_and_shoes(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def two_category_clothes_and_dress(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def two_category_clothes_and_accessories(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def two_category_clothes_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def two_category_shoes_and_dress(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def two_category_shoes_and_accessories(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def two_category_shoes_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def two_category_dress_and_accessories(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def two_category_dress_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def two_category_accessories_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def three_category_clothes_and_shoes_and_dress(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def three_category_clothes_and_shoes_and_accessories(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def three_category_clothes_and_shoes_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен'")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def three_category_clothes_and_dress_and_accessories(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def three_category_clothes_and_dress_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def three_category_clothes_and_accessories_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def three_category_shoes_and_dress_and_accessories(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def three_category_shoes_and_dress_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def three_category_shoes_and_accessories_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def three_category_dress_and_accessories_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен'")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def fourth_category_clothes_and_shoes_and_dress_and_accessories(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def fourth_category_clothes_and_shoes_and_dress_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def fourth_category_clothes_and_shoes_and_accessories_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def fourth_category_clothes_and_dress_and_accessories_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары'  and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def fourth_category_shoes_and_dress_and_accessories_and_jeans_blouses_skirts(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation

    def three_hundred(self):
        with self.db as cursor:
            cursor.execute("SELECT * FROM three_hundred WHERE `Подписка`='Да' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return transformation
