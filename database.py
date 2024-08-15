from motor.motor_asyncio import AsyncIOMotorClient
from data.config import MONGO_URI, DATABASE_NAME
from datetime import datetime
import feedparser


class Base(object):
    """Static class for base database manipulations."""
    DATABASE = None

    @staticmethod
    def init() -> None:
        client = AsyncIOMotorClient(MONGO_URI)
        Base.DATABASE = client[DATABASE_NAME]

    @staticmethod
    async def insert(collection, data) -> None:
        await Base.DATABASE[collection].insert_one(data)

    @staticmethod
    async def find_one(collection, query) -> list:
        return await Base.DATABASE[collection].find_one(query)

    @staticmethod
    async def find(collection, query) -> list:
        return await Base.DATABASE[collection].find(query)

    @staticmethod
    async def update_one(collection, query, new_values) -> None:
        await Base.DATABASE[collection].update_one(query, new_values)

    @staticmethod
    async def update_many(collection, query, new_values) -> None:
        await Base.DATABASE[collection].update_many(query, new_values)

    @staticmethod
    async def get_all(collection) -> list:
        return await Base.DATABASE[collection].find().to_list(length=None)


class Database(Base):
    """Static class for specific database manipulations."""

    @staticmethod
    async def user_exist(id: int) -> bool:
        user = await Database.find_one('users', {'id': id})
        return user is not None

    @staticmethod
    async def add_user(id: int, fullname: str, username: str) -> None:
        timestamp = round(datetime.utcnow().timestamp())
        await Database.insert('users', {'id': id, 'fullname': fullname, 'username': username, 'timestamp': timestamp})

    @staticmethod
    async def channel_exist(id: int, rss: str):
        channel = await Database.find_one('channels', {'id': id, 'rss': rss})
        return channel is not None

    @staticmethod
    async def add_channel(id: int, rss: str) -> dict:
        timestamp = round(datetime.utcnow().timestamp())
        response = feedparser.parse(rss)

        title = response.feed.title if response.feed.title is not None \
            else rss.split('/')[2]  # Title, but if title dont exist titile is domain name

        link = response.feed.link if response.feed.link is not None \
            else rss
        data = {'id': id, 'site': link, 'rss': rss, 'title': title, 'timestamp': timestamp}
        await Database.insert('channels', data)
        return data

    @staticmethod
    async def get_all_channels() -> list[dict]:
        channels = await Database.get_all('channels')
        return channels
