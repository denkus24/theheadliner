# The Headliner

**The Headliner** is a Telegram bot for reading RSS.

Bot is available by the [link](https://t.me/theheadlinerbot)  in Telegram

## Technology stack

- [*Python*](https://www.python.org/)
- [*Aiogram*](https://docs.aiogram.dev/en/latest/)
- [*Motor*](https://motor.readthedocs.io/en/stable/) (Asynchronous Python driver for MongoDB)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

Also fill in the ```.env``` file with your values.

You can configure the delay time and supported languages in the ```config.py``` file.

## Usage

Use the following commands to interact with the bot.

###  Client commands
* ```/start``` - Displays a welcome message and displays a keyboard for convenient interaction.

* ```/settings``` - Allows the user to disable notifications and contact an admin.

* ```/channels``` - Displays a list of channels to which the user is subscribed, and also allows you to unsubscribe from them when clicked.

* ```/add_channel``` - After entering the command, the user can enter the URL of the RSS feed, after which it will be added to the newsletter.

Also the user can add the feed by simply sending the URL to the user.

### Admin commands

* ```/sender``` - After entering the command, the bot asks for a message that will be sent to all users of the bot

* ```/statistic``` - Displays information about access to the database and the number of users.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)