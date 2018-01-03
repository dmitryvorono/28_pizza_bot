# Telegram Bot for Pizzeria

This project is telegram bot for a pizzeria that wants to be closer to its customers. It allows them to view the menu of the pizzeria in their phone.

# How to install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
$ pip install -r requirements.txt # alternatively try pip3
```
Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# How to Use

1. Export some environment variables:

`FLASK_DB_FILENAME` - path to your database
`FLASK_ADMIN` - username superuser
`FLASK_PASSWORD` - password superuser

2. You need export data from models.py to your database:

```#!bash
python db_create.py
python db_migraty.py
python db_load.py
```

3. Run flask-application to change menu:

```#!bash
python server.py
```

App will running on http://localhost:8080/admin/

4. Register new telegram bot for development purposes, get the new token. [@BotFather](https://telegram.me/botfather)
5. Export your telegram bot token to environment variable `BOT_TOKEN`
6. Launch bot:

```#!bash
python bot.py
```

# Bot commands

The bot understand two commands:
1. `/start` - show greetings
2. `/menu` - show menu

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
