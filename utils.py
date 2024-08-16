import asyncio

import aiogram.exceptions
from aiogram import Bot
import feedparser
import logging


async def send_info(bot: Bot, user_id: int, rss_url: str, title: str) -> None:
    """Function for sending RSS content"""

    resp = feedparser.parse(rss_url)
    logging.info(F"Sending RSS content {title} to user {user_id}")
    for entry in resp.entries:
        try:
            message = (f'<b>{title}</b>\n'
                       f'<a href="{entry.link}">{entry.title}</a>\n\n'
                       f'{entry.summary}\n\n'
                       f'<i>{entry.published}</i>')

            await bot.send_message(chat_id=user_id, text=message, parse_mode='HTML')
        except aiogram.exceptions.TelegramRetryAfter as e:
            logging.info(f'Sending RSS content {title} to user {user_id} sleep {e.retry_after} seconds')

            await asyncio.sleep(e.retry_after)
            continue
        except Exception as e:
            logging.error(f'Sending RSS content {title} to user {user_id} finished due error:{e}')
