import pymysql
import utils


class Script_work_with_database:
    connection = pymysql.connect(host=" ",
                                 user=" ",
                                 password=" ",
                                 db=" ")

    def mailing_to_all_categories(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на все категории: {}'.format(', '.join(transformation))

    def one_category_clothes(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на одну категорию одежда: {}'.format(', '.join(transformation))

    def one_category_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на одну категорию джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def one_category_shoes(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на одну категорию обувь: {}'.format(', '.join(transformation))

    def one_category_dress(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на одну категорию платья: {}'.format(', '.join(transformation))

    def one_category_accessories(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на одну категорию аксессуары: {}'.format(', '.join(transformation))

    def two_category_clothes_and_shoes(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на две категории одежда и обувь: {}'.format(', '.join(transformation))

    def two_category_clothes_and_dress(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на две категории одежда и платья: {}'.format(', '.join(transformation))

    def two_category_clothes_and_accessories(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на две категории одежда и аксессуары: {}'.format(', '.join(transformation))

    def two_category_clothes_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на две категории одежда и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def two_category_shoes_and_dress(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на две категории обувь и платья: {}'.format(', '.join(transformation))

    def two_category_shoes_and_accessories(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на две категории обувь и аксессуары: {}'.format(', '.join(transformation))

    def two_category_shoes_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на две категории обувь и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def two_category_dress_and_accessories(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на две категории платья и аксессуары: {}'.format(', '.join(transformation))

    def two_category_dress_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на две категории платья и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def two_category_accessories_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на две категории аксессуары и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def three_category_clothes_and_shoes_and_dress(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на три категории одежда и обувь и платья: {}'.format(', '.join(transformation))

    def three_category_clothes_and_shoes_and_accessories(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на три категории одежда, обувь и аксессуары: {}'.format(', '.join(transformation))

    def three_category_clothes_and_shoes_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен'")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на три категории одежда, обувь и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def three_category_clothes_and_dress_and_accessories(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на три категории одежда, платья и аксессуары: {}'.format(', '.join(transformation))

    def three_category_clothes_and_dress_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на три категории одежда, платья и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def three_category_clothes_and_accessories_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на три категории одежда, аксессуары и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def three_category_shoes_and_dress_and_accessories(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на три категории обувь, платья и аксессуары: {}'.format(', '.join(transformation))

    def three_category_shoes_and_dress_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на три категории обувь, платья и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def three_category_shoes_and_accessories_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на три категории обувь, аксессуары и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def three_category_dress_and_accessories_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен'")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на три категории платья, аксессуары и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def fourth_category_clothes_and_shoes_and_dress_and_accessories(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='удалено Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на четыре категории одежда, обувь, платья и аксессуары: {}'.format(', '.join(transformation))

    def fourth_category_clothes_and_shoes_and_dress_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='удалено Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на четыре категории одежда, обувь, платья и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def fourth_category_clothes_and_shoes_and_accessories_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='удалено Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на четыре категории одежда, обувь, аксессуары и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def fourth_category_clothes_and_dress_and_accessories_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='удалено Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары'  and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на четыре категории одежда, платья, аксессуары и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def fourth_category_shoes_and_dress_and_accessories_and_jeans_blouses_skirts(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM table_shop WHERE `Верхняя одежда`='удалено Верхняя одежда' and `Джинсы, блузки, юбки`='Джинсы, блузки, юбки' and `Обувь`='Обувь' and `Платья`='Платья' and `Аксессуары`='Аксессуары' and `Остановка бота`='Запущен' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на четыре категории обувь, платья, аксессуары и джинсы, блузки, юбки: {}'.format(', '.join(transformation))

    def three_hundred(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM three_hundred WHERE `Подписка`='Да' ")
            category = cursor.fetchall()
            transformation = [x[0] for x in category]
            return 'Подписка на рассылку за 300: {}'.format(', '.join(transformation))


q = Script_work_with_database()
print(q.mailing_to_all_categories())
print(q.one_category_clothes())
print(q.one_category_shoes())
print(q.one_category_dress())
print(q.one_category_accessories())
print(q.one_category_jeans_blouses_skirts())
print(q.two_category_clothes_and_shoes())
print(q.two_category_clothes_and_dress())
print(q.two_category_clothes_and_accessories())
print(q.two_category_clothes_and_jeans_blouses_skirts())
print(q.two_category_shoes_and_dress())
print(q.two_category_shoes_and_accessories())
print(q.two_category_shoes_and_jeans_blouses_skirts())
print(q.two_category_dress_and_accessories())
print(q.two_category_dress_and_jeans_blouses_skirts())
print(q.two_category_accessories_and_jeans_blouses_skirts())
print(q.three_category_clothes_and_shoes_and_dress())
print(q.three_category_clothes_and_shoes_and_accessories())
print(q.three_category_clothes_and_shoes_and_jeans_blouses_skirts())
print(q.three_category_clothes_and_dress_and_accessories())
print(q.three_category_clothes_and_dress_and_jeans_blouses_skirts())
print(q.three_category_clothes_and_accessories_and_jeans_blouses_skirts())
print(q.three_category_shoes_and_dress_and_accessories())
print(q.three_category_shoes_and_dress_and_jeans_blouses_skirts())
print(q.three_category_shoes_and_accessories_and_jeans_blouses_skirts())
print(q.three_category_dress_and_accessories_and_jeans_blouses_skirts())
print(q.fourth_category_clothes_and_shoes_and_dress_and_accessories())
print(q.fourth_category_clothes_and_shoes_and_dress_and_jeans_blouses_skirts())
print(q.fourth_category_clothes_and_shoes_and_accessories_and_jeans_blouses_skirts())
print(q.fourth_category_clothes_and_dress_and_accessories_and_jeans_blouses_skirts())
print(q.fourth_category_shoes_and_dress_and_accessories_and_jeans_blouses_skirts())
print(q.three_hundred())

"""
Подписка на все категории:

Подписка на одну категорию одежда:
Подписка на одну категорию обувь:
Подписка на одну категорию платья:
Подписка на одну категорию аксессуары:
Подписка на одну категорию джинсы, блузки, юбки:

Подписка на две категории одежда и обувь:
Подписка на две категории одежда и платья:
Подписка на две категории одежда и аксессуары:
Подписка на две категории одежда и джинсы, блузки, юбки:
Подписка на две категории обувь и платья:
Подписка на две категории обувь и аксессуары:
Подписка на две категории обувь и джинсы, блузки, юбки:
Подписка на две категории платья и аксессуары:
Подписка на две категории платья и джинсы, блузки, юбки:
Подписка на две категории аксессуары и джинсы, блузки, юбки:

Подписка на три категории одежда, обувь и платья:
Подписка на три категории одежда, обувь и аксессуары:
Подписка на три категории одежда, обувь и джинсы, блузки, юбки:
Подписка на три категории одежда, платья и аксессуары:
Подписка на три категории одежда, платья и джинсы, блузки, юбки:
Подписка на три категории одежда, аксессуары и джинсы, блузки, юбки:
Подписка на три категории обувь, платья и аксессуары:
Подписка на три категории обувь, платья и джинсы, блузки, юбки:
Подписка на три категории обувь, аксессуары и джинсы, блузки, юбки:
Подписка на три категории платья, аксессуары и джинсы, блузки, юбки:

Подписка на четыре категории одежда, обувь, платья и аксессуары:
Подписка на четыре категории одежда, обувь, платья и джинсы, блузки, юбки:
Подписка на четыре категории одежда, обувь, аксессуары и джинсы, блузки, юбки:
Подписка на четыре категории одежда, платья, аксессуары и джинсы, блузки, юбки:
Подписка на четыре категории обувь, платья, аксессуары и джинсы, блузки, юбки:
"""





