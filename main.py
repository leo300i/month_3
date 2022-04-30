from aiogram import executor
from config import dp, Url, bot
import logging
from handlers import callback, client, notification, fsmAdminMenu, fsmAdminGetUser, inline
from database import bot_DB
from decouple import config


async def on_start_up(_):
    await bot.set_webhook(Url)
    bot_DB.sql_create()


async def on_shutdown(dp):
    await bot.delete_webhook()


client.register_hendlers_client(dp)
callback.register_hendlers_callback(dp)
inline.register_handler_Inline(dp)
fsmAdminGetUser.register_hendler_fsmAdminGetUser(dp)
fsmAdminMenu.register_hendler_fsmAdminGetUser(dp)

notification.register_hendlers_notification(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False, on_startup=on_start_up)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_startup=on_start_up(),
        on_shutdown=on_shutdown(),
        skip_updates=True,
        host="0.0.0.0",
        port=int(config("port", default=5000))
    )
