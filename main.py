import os
from datetime import time
import telebot
from telebot import types
import sys

bot = telebot.TeleBot('1088072428:AAFqdu8gyHGKSG88-oYeDsasmbMA4k0lr5o')


@bot.message_handler(commands=['start'])
def start(message):
    sticker = open('sticker/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('45')
    btn2 = types.KeyboardButton('Начальник камчатки')
    btn3 = types.KeyboardButton('Это Не Любовь')
    btn4 = types.KeyboardButton('Ночь')
    btn5 = types.KeyboardButton('Группа крови')
    btn6 = types.KeyboardButton('Последний герой')
    btn7 = types.KeyboardButton('Звезда По Имени Солнце')
    btn8 = types.KeyboardButton('Черный альбом')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    send_mess = f"<b>Привет {message.from_user.first_name}</b>!\nКакой альбом вас " \
                f"интересует? "
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "начать тест заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('45')
        btn2 = types.KeyboardButton('Начальник камчатки')
        btn3 = types.KeyboardButton('Это Не Любовь')
        btn4 = types.KeyboardButton('Ночь')
        btn5 = types.KeyboardButton('Группа крови')
        btn6 = types.KeyboardButton('Последний герой')
        btn7 = types.KeyboardButton('Звезда По Имени Солнце')
        btn8 = types.KeyboardButton('Черный альбом')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        final_message = "Решил послушать какой-то другой? \nКакие альбомы вас интересуют?:"

    elif get_message_bot == "45":
        markup = types.InlineKeyboardMarkup()
        img = open('pictures/45.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        music1 = open('45 album/Алюм огурцы.mp3', 'rb')
        bot.send_audio(message.chat.id, music1, timeout=10)
        music2 = open('45 album/Асфальт.mp3', 'rb')
        bot.send_audio(message.chat.id, music2, timeout=10)
        music3 = open('45 album/Бездельник.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('45 album/битник.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('45 album/Восьмиклас.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('45 album/Время,деньги.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('45 album/Дерево.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('45 album/Мои друзья.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('45 album/На кухне.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('45 album/Просто хочешь.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('45 album/Ситар.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('45 album/Солнеч дни.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('45 album/Электричка.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        final_message = "Выбирайте песню, которую вы хотите послушать"

    elif get_message_bot == 'начальник камчатки':
        markup = types.InlineKeyboardMarkup()
        img = open('pictures/Начальник камчатки.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        music1 = open('Начальник камчатки/Ария мистера Икс.mp3', 'rb')
        bot.send_audio(message.chat.id, music1, timeout=10)
        music2 = open('Начальник камчатки/Генерал.mp3', 'rb')
        bot.send_audio(message.chat.id, music2, timeout=10)
        music3 = open('Начальник камчатки/Гость.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Начальник камчатки/Дождь для нас.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Начальник камчатки/Каждую ночь.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Начальник камчатки/Камчатка.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Начальник камчатки/Последний герой.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Начальник камчатки/Прогулка романтика.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Начальник камчатки/Растопите снег.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Начальник камчатки/Саша.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Начальник камчатки/Сюжет для новой песни.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Начальник камчатки/Транквилизатор.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Начальник камчатки/Троллейбус.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Начальник камчатки/Хочу быть с тобой.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        final_message = "Выбирайте песню, которую вы хотите послушать"

    elif get_message_bot == 'это не любовь':
        markup = types.InlineKeyboardMarkup()
        img = open('pictures/это не любовь.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        music1 = open('Это не любовь/Безъядерная зона.mp3', 'rb')
        bot.send_audio(message.chat.id, music1, timeout=10)
        music2 = open('Это не любовь/Верь мне.mp3', 'rb')
        bot.send_audio(message.chat.id, music2, timeout=10)
        music3 = open('Это не любовь/Весна.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Это не любовь/Город.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Это не любовь/Дети проходных дворов.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Это не любовь/Музыка волн.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Это не любовь/Несовременно.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Это не любовь/Саша.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Это не любовь/Уходи.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Это не любовь/Это любовь.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Это не любовь/Это не любовь.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        final_message = "Выбирайте песню, которую вы хотите послушать"

    elif get_message_bot == 'ночь':
        markup = types.InlineKeyboardMarkup()
        img = open('pictures/ночь.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        music1 = open('Ночь/Видели ночь.mp3', 'rb')
        bot.send_audio(message.chat.id, music1, timeout=10)
        music2 = open('Ночь/Жизнь в стеклах.mp3', 'rb')
        bot.send_audio(message.chat.id, music2, timeout=10)
        music3 = open('Ночь/Звезды остануться здесь.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Ночь/Мама анархия.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Ночь/Мы хотим танцевать.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Ночь/Ночь.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Ночь/Пора.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Ночь/Последний герой.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Ночь/Танец.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Ночь/Твой номер.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Ночь/Фильмы.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        final_message = "Выбирайте песню, которую вы хотите послушать"

    elif get_message_bot == 'группа крови':
        markup = types.InlineKeyboardMarkup()
        img = open('pictures/группа крови.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        music1 = open('Группа крови/Бошетунмай.mp3', 'rb')
        bot.send_audio(message.chat.id, music1, timeout=10)
        music2 = open('Группа крови/В Наших Глазах.mp3', 'rb')
        bot.send_audio(message.chat.id, music2, timeout=10)
        music3 = open('Группа крови/Война.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Группа крови/Группа крови.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Группа крови/Дальше действовать будем мы.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Группа крови/Закрой за мной дверь я ухожу.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Группа крови/Легенда.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Группа крови/Мама мы все сошли с ума.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Группа крови/Попробуй спеть вместе со мной.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Группа крови/Прохожий.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Группа крови/Спокойная Ночь.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        final_message = "Выбирайте песню, которую вы хотите послушать"

    elif get_message_bot == 'последний герой':
        markup = types.InlineKeyboardMarkup()
        img = open('pictures/последний геро.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        music1 = open('Последний герой/В Наших Глазах.mp3', 'rb')
        bot.send_audio(message.chat.id, music1, timeout=10)
        music2 = open('Последний герой/Война.mp3', 'rb')
        bot.send_audio(message.chat.id, music2, timeout=10)
        music3 = open('Последний герой/Группа крови.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Последний герой/Мама мы все сошли с ума.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Последний герой/Перемен.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Последний герой/Печаль.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Последний герой/Последний герой.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Последний герой/Спокойная Ночь.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Последний герой/Троллейбус.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Последний герой/Электричка.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        final_message = "Выбирайте песню, которую вы хотите послушать"

    elif get_message_bot == 'звезда по имени солнце':
        markup = types.InlineKeyboardMarkup()
        img = open('pictures/звезда.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        music1 = open('Звезда по имени солнце/Апрель.mp3', 'rb')
        bot.send_audio(message.chat.id, music1, timeout=10)
        music2 = open('Звезда по имени солнце/Велосипед.mp3', 'rb')
        bot.send_audio(message.chat.id, music2, timeout=10)
        music3 = open('Звезда по имени солнце/Звезда по имени солнце.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Звезда по имени солнце/Место для шага вперед.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Звезда по имени солнце/Невеселая песня.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Звезда по имени солнце/Пачка сигарет.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Звезда по имени солнце/Песня без слов.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Звезда по имени солнце/Печаль.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Звезда по имени солнце/Сказка.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Звезда по имени солнце/Стук.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        final_message = "Выбирайте песню, которую вы хотите послушать"

    elif get_message_bot == 'черный альбом':
        markup = types.InlineKeyboardMarkup()
        img = open('pictures/черный.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        music1 = open('Черный альбом/Завтра война.mp3', 'rb')
        bot.send_audio(message.chat.id, music1, timeout=10)
        music2 = open('Черный альбом/Звезда.mp3', 'rb')
        bot.send_audio(message.chat.id, music2, timeout=10)
        music3 = open('Черный альбом/Когда твоя девушка больна.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Черный альбом/Кончится Лето.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Черный альбом/Красно-желтые дни.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Черный альбом/Кукушка.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Черный альбом/Муравейник.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Черный альбом/Нам с тобой.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        music3 = open('Черный альбом/Следи за собой.mp3', 'rb')
        bot.send_audio(message.chat.id, music3, timeout=10)
        final_message = "Выбирайте песню, которую вы хотите послушать"

    # Здесь различные дополнительные проверки и условия
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('45')
        btn2 = types.KeyboardButton('Начальник камчатки')
        btn3 = types.KeyboardButton('Это Не Любовь')
        btn4 = types.KeyboardButton('Ночь')
        btn5 = types.KeyboardButton('Группа крови')
        btn6 = types.KeyboardButton('Последний герой')
        btn7 = types.KeyboardButton('Звезда По Имени Солнце')
        btn8 = types.KeyboardButton('Черный альбом')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        final_message = "Так, так, так\nПостой, лучше нажми на одну из интерактивных кнопок ниже"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)
