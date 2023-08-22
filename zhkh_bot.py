import asyncio
import datetime
from telegram import Bot
import creds

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = creds.bot_token

# Инициализация бота
bot = Bot(token=TOKEN)

# Замените 'YOUR_CHAT_ID' на ID чата, куда бот будет отправлять сообщения
chat_id = creds.chat_id

async def send_message():
    try:
        await bot.send_message(chat_id=chat_id, text="Привет! Это сообщение отправлено ботом.")
    except Exception as e:
        print("Ошибка при отправке сообщения:", e)

async def main():
    while True:
        now = datetime.datetime.now()

        # Проверяем, если сегодня 20 число и время 22:20
        if now.day == 22 and now.hour == 20 and now.minute == 35:
            await send_message()

            # Ожидание до следующего месяца
            next_month = now.month + 1 if now.month < 12 else 1
            next_year = now.year + 1 if now.month == 12 else now.year
            next_date = now.replace(year=next_year, month=next_month, day=20, hour=22, minute=20)

            sleep_seconds = (next_date - now).seconds
            await asyncio.sleep(sleep_seconds)

        # Ожидание до следующей минуты
        next_minute = now + datetime.timedelta(minutes=1)
        sleep_seconds = (next_minute - now).seconds
        await asyncio.sleep(sleep_seconds)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())