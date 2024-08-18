from aiogram import Bot, Dispatcher
from logging.handlers import TimedRotatingFileHandler
from data.config import BOT_API, HOUR_DELAY
from database import Database
from handlers.client import start, add_channel, back, channels_list
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from middlewares import AutoLanguageMiddleware

import asyncio
import logging
import send_info


async def main():
    bot = Bot(token=BOT_API)
    dp = Dispatcher()
    Database.init()
    scheduler = AsyncIOScheduler()
    scheduler.start()

    # Setting up sending for users
    scheduler.add_job(func=send_info.send_info,
                      kwargs={'bot': bot},
                      trigger='interval',
                      minutes=HOUR_DELAY)

    dp.include_routers(
        back.router,
        start.router,
        add_channel.router,
        channels_list.router
    )

    dp.message.middleware(AutoLanguageMiddleware())
    dp.callback_query.middleware(AutoLanguageMiddleware())

    await dp.start_polling(bot, scheduler=scheduler)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        handlers=[logging.StreamHandler(),
                                  TimedRotatingFileHandler(f"logs/log", when='midnight', interval=1, backupCount=5)],
                        encoding='utf-8', format='[ %(asctime)s ](%(levelname)s) %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S')
    asyncio.run(main())
