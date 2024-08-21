from aiogram import html

welcome_message = {
    "uk": f"{html.bold('Ласкаво просимо!')}\n\nЯ - бот що допоможе тобі слідкувати за новинами, анонсами, блогами і т.д. за допомгою {html.bold('RSS')}.\n"
          f"Додай канал вже зараз за допомогою кнопки внизу, або уведи його URL 👇",
    "en": f"{html.bold('Welcome!')}\n\nI am a bot that will help you keep up with news, announcements, blogs, etc. {html.bold('RSS')}.\n"
          f"Add a channel now for additional help buttons below, or input URL 👇",
    "ru": f"{html.bold('Добро пожаловать!')}\n\nЯ - бот, который поможет тебе следить за новостями, анонсами, блогами и т.д. с помощью {html.bold('RSS')}.\n"
          f"Добавь канал уже сейчас с помощью кнопки внизу, или введи его URL 👇"}

start_message = {"uk": f"{html.bold('Привіт!')}\n"
                       f"Бот безкоштовний, але ви завжди можете підтримати розробника чашечкою кави 😉\n\n"
                       f"{html.bold('BTC:')} {html.code('bc1qqelnrjvc0tdhmpjlrqkskzlu3p9cx5605q99s5')}\n"
                       f"{html.bold('ETH:')} {html.code('0x8806c77fA2EA69A56Cd6E19d6451E3ebF3c7753e')}\n"
                       f"{html.bold('BCH:')} {html.code('qq98nxzs9pz86qv4py9fwwcjyten7fhrvc4z8hmyyk')}\n\n"
                       f"Кнопки для взаємодії внизу 👇",
                 "en": f"{html.bold('Hello!')}\n"
                       f"The bot is free, but you can always support the developer with a cup of coffee 😉\n\n"
                       f"{html.bold('BTC:')} {html.code('bc1qqelnrjvc0tdhmpjlrqkskzlu3p9cx5605q99s5')}\n"
                       f"{html.bold('ETH:')} {html.code('0x8806c77fA2EA69A56Cd6E19d6451E3ebF3c7753e')}\n"
                       f"{html.bold('BCH:')} {html.code('qq98nxzs9pz86qv4py9fwwcjyten7fhrvc4z8hmyyk')}\n\n"
                       f"Interaction buttons below 👇",
                 "ru": f"{html.bold('Привет!')}\n"
                       f"Бот бесплатный, но вы всегда можете поддержать разработчика чашечкой кофе 😉\n\n"
                       f"{html.bold('BTC:')} {html.code('bc1qqelnrjvc0tdhmpjlrqkskzlu3p9cx5605q99s5')}\n"
                       f"{html.bold('ETH:')} {html.code('0x8806c77fA2EA69A56Cd6E19d6451E3ebF3c7753e')}\n"
                       f"{html.bold('BCH:')} {html.code('qq98nxzs9pz86qv4py9fwwcjyten7fhrvc4z8hmyyk')}\n\n"
                       f"Кнопки для взаимодействия внизу 👇"}

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

press_on_channel = {
    'uk': 'Натисніть на канал, якщо хочете скасувати підписку',
    'en': 'Press on channel if you want to unsubscribe',
    'ru': 'Нажмите на канал, если хотите отписаться'
}

channel_alerady_existing = {
    "uk": "Канал вже існує.",
    "en": "Channel already existing.",
    "ru": "Канал уже существует."
}

url_is_invalid = {
    "uk": "❌ Неправильний URL. Будь ласка, перевірте його та спробуйте знову.",
    "en": "❌ URL is invalid. Please check it and try again.",
    "ru": "❌ Неверный URL. Пожалуйста, проверьте его и попробуйте снова."
}

error_while_adding = {
    "uk": "❌ Помилка під час додавання каналу.",
    "en": "❌ Error while adding channel.",
    "ru": "❌ Ошибка при добавлении канала."
}

adding_channel = {'uk': 'Додавання каналу...',
                  'en': 'Adding channel...',
                  'ru': 'Добавление канала...'}


def feed_added(user_lang: str, channel_title: str) -> str:
    match user_lang:
        case 'uk':
            return f'✅ Стрічка {channel_title} додана успішно'
        case 'en':
            return f"✅ Feed {channel_title} added successfully"
        case 'ru':
            return f"✅ Лента {channel_title} добавлена успешно"


adding_channel = {'uk': 'Ви ще не додали жодного каналу 😔',
                  'en': "You haven't added any channel yet 😔",
                  'ru': 'Вы ещё не добавили ни одного канала 😔'}
