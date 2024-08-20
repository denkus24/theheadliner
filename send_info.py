from aiogram import Bot
from utils import convert_to_timestamp, max_date
from database import Database

import asyncio
import aiogram.exceptions
import feedparser
import logging


async def send_info(bot: Bot) -> None:
    """Function for sending RSS content"""
    channels = await Database.get_all_channels()
    disabled_users = await Database.get_users_with_disabled_notifications()
    for channel in channels:
        _id, user_id, site, rss, title, last_timestamp = channel.values()
        if user_id not in disabled_users:
            resp = feedparser.parse(rss)  # Parsing rss url

            last_entry_timestamp = max_date(resp.entries)
            if last_entry_timestamp != last_timestamp:
                await Database.update_channel_last_update(user_id, rss, last_entry_timestamp)
            logging.info(F"Sending RSS content {title} to user {user_id}")
            for entry in resp.entries:
                try:
                    entry_timestamp = convert_to_timestamp(entry.published)
                    if entry_timestamp > last_timestamp:  # Compare timestamp with last update
                        message = (f'<b>{title}</b>\n'
                                   f'<a href="{entry.link}">{entry.title}</a>\n\n'
                                   f'{entry.summary}\n\n'
                                   f'<i>{entry.published}</i>')

                        await bot.send_message(chat_id=user_id, text=message, parse_mode='HTML')
                except aiogram.exceptions.TelegramRetryAfter as e:
                    logging.info(f'Sending RSS content "{title}" to user {user_id} sleep {e.retry_after} seconds')

                    await asyncio.sleep(e.retry_after)
                    continue
                except Exception as e:
                    logging.error(f'Sending RSS content "{title}" to user {user_id} finished due error:{e}')
        else:
            logging.info(f'Sending RSS content {title} to user {user_id} finished due blocking notifications')
