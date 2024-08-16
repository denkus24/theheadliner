from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from data.config import SUPPORTABLE_LANGUAGES


class AutolanguageMidleware(BaseMiddleware):
    """Middleware for customizing the user language"""

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        language_code = data['event_context'].user.language_code
        data['event_context'].user.language_code = language_code if language_code in SUPPORTABLE_LANGUAGES else 'en'
        return await handler(event, data)
