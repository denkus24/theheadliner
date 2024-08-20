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

channel_added = {"uk": "✅ Канал додано",
                 "en": "✅ Channel added",
                 "ru": "✅ Канал добавлен"}

turned_back = {"uk": html.quote("Ви повернулись назад"),
               "en": html.quote("You turned back"),
               "ru": html.quote("Вы вернулись назад")}

channel_deleted = {"uk": '✅ Канал видалено',
                   "en": '✅ Channel deleted',
                   "ru": '✅ Канал удалено'}

choose_setting = {"uk": 'Оберіть налаштування, що хочете змінити',
                  "en": 'Choose option what you want to change',
                  "ru": 'Выберите опцию что хотите сменить'}

enable_messages = {"uk": '🔴 Повідомлення вимкнені',
                   "en": '🔴 Notifications disabled',
                   "ru": '🔴 Уведомления отключены'}

disable_messages = {"uk": '🟢 Повідомлення увімкнені',
                    "en": '🟢 Notifications enabled',
                    "ru": '🟢 Уведомления включены'}

write_to_developer = {"uk": '✍️ Написати розробнику',
                      "en": '✍️ Write to developer',
                      "ru": '✍️ Написать разработчику'}

write_message_for_dev = {"uk": 'Уведіть ваше питання розробнику',
                         "en": 'Write message for developer',
                         "ru": 'Напишите ваш вопрос разработчику'}

your_message_was_sent = {
    "uk": f'{html.bold("Ваше повідомлення було відправлено розробнику.")}\nВи отримаєте відповідь згодом.',
    "en": f'{html.bold("Your message has been sent to the developer.")}\nYou will receive a reply shortly.',
    "ru": f'{html.bold("Ваше сообщение было отправлено разработчику.")}\nВы получите ответ в ближайшее время.'
}

developer_answer = {
    'uk': html.bold('Відповідь від розробника:'),
    'en': html.bold('Answer from developer:'),
    'ru': html.bold('Ответ от разработчика:')
}
