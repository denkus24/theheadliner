from motor.motor_asyncio import AsyncIOMotorClient
from data.config import MONGO_URI, DATABASE_NAME
from datetime import datetime
from bson import ObjectId

import utils
import feedparser


class Base(object):
    """Static class for base database manipulations."""
    DATABASE = None
    CLIENT = None

    @staticmethod
    def init() -> None:
        Base.CLIENT = AsyncIOMotorClient(MONGO_URI)
        Base.DATABASE = Base.CLIENT[DATABASE_NAME]

    @staticmethod
    async def insert(collection, data) -> None:
        await Base.DATABASE[collection].insert_one(data)

    @staticmethod
    async def find_one(collection, query) -> dict:
        result: dict = await Base.DATABASE[collection].find_one(query)
        return result

    @staticmethod
    async def find(collection, query) -> list:
        return Base.DATABASE[collection].find(query)

    @staticmethod
    async def update_one(collection, query, new_values) -> None:
        await Base.DATABASE[collection].update_one(query, new_values)

    @staticmethod
    async def update_many(collection, query, new_values) -> None:
        await Base.DATABASE[collection].update_many(query, new_values)

    @staticmethod
    async def delete_one(collection, query) -> None:
        await Base.DATABASE[collection].delete_one(query)

    @staticmethod
    async def delete_many(collection, query) -> None:
        await Base.DATABASE[collection].delete_many(query)

    @staticmethod
    async def get_all(collection) -> list:
        return await Base.DATABASE[collection].find().to_list(length=None)

    @staticmethod
    async def count(collection, query) -> int:
        return await Base.DATABASE[collection].count_documents(query)

    @staticmethod
    async def ping() -> bool:
        res = await Base.CLIENT.admin.command('ping')
        return bool(res)


class Database(Base):
    """Static class for specific database manipulations."""

    @staticmethod
    async def user_exist(id: int) -> bool:
        user = await Database.find_one('users', {'id': id})
        return user is not None

    @staticmethod
    async def add_user(id: int, fullname: str, username: str) -> None:
        timestamp = round(datetime.utcnow().timestamp())
        await Database.insert('users', {'id': id, 'fullname': fullname, 'username': username, 'timestamp': timestamp,
                                        'message_enabled': True})

    @staticmethod
    async def channel_exist(id: int, rss: str) -> bool:
        channel = await Database.find_one('channels', {'id': id, 'rss': rss})
        return channel is not None

    @staticmethod
    async def add_channel(id: int, rss: str) -> dict:
        response = feedparser.parse(rss)

        last_update = utils.max_date(response.entries)

        title = response.feed.title if response.feed.title is not None \
            else rss.split('/')[2]  # Title, but if title dont exist titile is domain name

        link = response.feed.link if response.feed.link is not None \
            else rss

        data = {'id': id, 'site': link, 'rss': rss, 'title': title, 'last_update': last_update}

        await Database.insert('channels', data)
        return data

    @staticmethod
    async def get_user_channels(id: int) -> list:
        cursor = await Database.find('channels', {'id': id})
        channels = await cursor.to_list(length=None)
        return channels

    @staticmethod
    async def get_all_channels() -> list[dict]:
        channels = await Database.get_all('channels')
        return channels

    @staticmethod
    async def update_channel_last_update(id: int, url: str, timestamp: int) -> None:
        await Database.update_one('channels', {'id': id, 'rss': url}, {'$set': {'last_update': timestamp}})

    @staticmethod
    async def delete_channel(id: str) -> None:
        await Database.delete_one('channels', {'_id': ObjectId(id)})

    @staticmethod
    async def is_user_notifications_enabled(id: int) -> bool:
        user = await Database.find_one('users', {'id': id})
        return user['message_enabled']

    @staticmethod
    async def update_user_notification(id: int, state: bool) -> None:
        await Database.update_one('users', {'id': id}, {'$set': {'message_enabled': state}})

    @staticmethod
    async def get_users_with_disabled_notifications() -> list:
        users = await Database.get_all('users')
        result = []
        for user in users:
            if not user['message_enabled']:
                result.append(user['id'])
        return result

    @staticmethod
    async def get_user_ids() -> list:
        users = await Database.get_all('users')
        result = [user['id'] for user in users]
        return result

    @staticmethod
    async def get_number_of_users() -> int:
        return await Database.count('users', {})

    @staticmethod
    async def clear_users_channels(id: int) -> None:
        await Database.delete_many('channels', {'id': id})
