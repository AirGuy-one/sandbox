import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from files_operations import download_file_by_url

TOKEN = '7113844511:AAGjU6NHn23U9BXZ1C0lSlU5vvMkoE7OYC4'

dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {message.from_user.full_name}!")


@dp.message()
async def photo_handler(message: Message) -> None:
    """
    This handler receives photos sent by the user
    """
    if message.photo:
        tg_server_file_info = await bot.get_file(message.photo[-1].file_id)
        tg_server_file_path = tg_server_file_info.file_path
        url = f'https://api.telegram.org/file/bot{TOKEN}/{tg_server_file_path}'

        await download_file_by_url(url=url)
    else:
        await message.answer(message.text)
    await message.answer("Photo received and saved!")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
