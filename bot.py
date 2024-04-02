import asyncio
import logging

from aiogram import Bot, Dispatcher

import config
import handlers


async def main():
    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()
    dp.include_router(handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    print('Bot`s started')
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
