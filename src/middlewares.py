from typing import Callable, Dict, Any, Awaitable, Union
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from data.config import SUPPORTABLE_LANGUAGES
from aiogram.dispatcher.middlewares.user_context import EVENT_FROM_USER_KEY


class AutoLanguageMiddleware(BaseMiddleware):
    """Middleware for customizing the user language"""

    async def __call__(
            self,
            handler: Callable[[Union[Message, CallbackQuery], Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        user_language_code = data[EVENT_FROM_USER_KEY].language_code if data[EVENT_FROM_USER_KEY].language_code in SUPPORTABLE_LANGUAGES else 'en'
        data['user_lang']: str = user_language_code
        return await handler(event, data)
