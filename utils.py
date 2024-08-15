import asyncio

import aiogram.exceptions
from aiogram import Bot
import feedparser
import logging

async def send_info(bot: Bot, user_id: int, rss_url: str, title: str) -> None:
    resp = feedparser.parse(rss_url)
    for entry in resp.entries:
        try:
            message = (f'<b>{title}</b>\n'
                       f'<a href="{entry.link}">{entry.title}</a>\n\n'
                       f'{entry.summary}\n\n'
                       f'<i>{entry.published}</i>')

            await bot.send_message(chat_id=user_id, text=message, parse_mode='HTML')
        except Exception as e:
            if isinstance(e, aiogram.exceptions.TelegramRetryAfter):
                logging.info('Sending sleep')
                await asyncio.sleep(e.retry_after)
                continue

