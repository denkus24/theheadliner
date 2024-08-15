from aiogram import Bot, Dispatcher
from logging.handlers import TimedRotatingFileHandler
from data.config import BOT_API
from database import Database
from handlers.client import start, add_channel, back
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import asyncio
import logging
import sys
import utils

logging.basicConfig(level=logging.INFO,
                    handlers=[
                        # logging.FileHandler(f"logs/{datetime.date.today()}.log"),
                        logging.StreamHandler(),
                        TimedRotatingFileHandler(f"logs/log", when='midnight', interval=1, backupCount=5)

                    ], encoding='utf-8', format='[ %(asctime)s ](%(levelname)s) %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S')


async def main():
    bot = Bot(token=BOT_API)
    dp = Dispatcher()
    Database.init()
    scheduler = AsyncIOScheduler()
    scheduler.start()
    channels = await Database.get_all_channels()
    for channel in channels:
        scheduler.add_job(func=utils.send_info,
                          kwargs={'bot': bot,
                                  'user_id': channel['id'],
                                  'rss_url': channel['rss'],
                                  'title': channel['title']},
                          trigger='interval',
                          hours=1)

    dp.include_routers(
        back.router,
        start.router,
        add_channel.router,
    )

    await dp.start_polling(bot, scheduler=scheduler)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
