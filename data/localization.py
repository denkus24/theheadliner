from aiogram import html

welcome_message = {
    "uk": f"{html.bold('Ласкаво просимо!')}\nЯ - бот що допоможе тобі слідкувати за новинами, анонсами, блогами і т.д. за допомгою {html.bold('RSS')}.\nДодай канал вже зараз за допомогою кнопки внизу 👇",
    "en": f"{html.bold('Welcome!')}\nI am a bot that will help you keep up with news, announcements, blogs, etc. {html.bold('RSS')}.\nAdd a channel now for additional help buttons below 👇",
    "ru": f"{html.bold('Добро пожаловать!')}\nЯ - бот, который поможет тебе следить за новостями, анонсами, блогами и т.д. с помощью {html.bold('RSS')}.\nДобавь канал уже сейчас с помощью кнопки внизу 👇"}

start_message = {"uk": f"{html.bold('Привіт!')}\nКнопки для взаємодії внизу 👇",
                 "en": f"{html.bold('Hello!')}\nButtons to interact at the bottom 👇",
                 "ru": f"{html.bold('Привет!')}\nКнопки для взаимодействия внизу 👇"}

add_channel = {"uk": "Додати канал",
               "en": "Add channel",
               "ru": "Добавить канал"}

my_channels = {"uk": "Мої канали",
               "en": "My channels",
               "ru": "Мои каналы"}

settings = {"uk": "Налаштування",
            "en": "Settings",
            "ru": "Настройки"}

enter_url = {"uk": "Уведіть URL",
             "en": "Enter URL",
             "ru": "Введите URL"}

back = {"uk": "Назад ⬅️",
        "en": "Back ⬅️",
        "ru": "Назад ⬅️"}

channel_added = {"uk": "Канал додано",
                 "en": "Channel added",
                 "ru": "Канал добавлен"}

turned_back = {"uk": html.quote("Ви повернулись назад"),
               "en": html.quote("You turned back"),
               "ru": html.quote("Вы вернулись назад")}

channel_deleted = {"uk": '✅ Канал видалено',
                   "en": '✅ Channel deleted',
                   "ru": '✅ Канал удалено'}
