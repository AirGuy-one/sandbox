from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram_tonconnect.handlers import AiogramTonConnectHandlers
from aiogram_tonconnect.middleware import AiogramTonConnectMiddleware

BOT_TOKEN = "1234567890:QWERTYUIOPASDFGHJKLZXCVBNM"

REDIS_DSN = "redis://localhost:6379/0"

# Link to your created manifest.json
MANIFEST_URL = "https://raw.githubusercontent.com/nessshon/aiogram-tonconnect/main/tonconnect-manifest.json"

# List of wallets to exclude
EXCLUDE_WALLETS = ["mytonwallet"]


async def main():
    # Initializing the storage for FSM (Finite State Machine)
    storage = RedisStorage.from_url(REDIS_DSN)

    # Creating a bot object with the token and HTML parsing mode
    bot = Bot(BOT_TOKEN, parse_mode="HTML")

    # Creating a dispatcher object using the specified storage
    dp = Dispatcher(storage=storage)

    # Registering middleware for TON Connect processing
    dp.update.middleware.register(
        AiogramTonConnectMiddleware(
            redis=storage.redis,
            manifest_url=MANIFEST_URL,
            exclude_wallets=EXCLUDE_WALLETS,
            qrcode_type="url",  # or "bytes" if you prefer to generate QR codes locally.
        )
    )

    # Registering TON Connect handlers
    AiogramTonConnectHandlers().register(dp)

    # Starting the bot using long polling
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())