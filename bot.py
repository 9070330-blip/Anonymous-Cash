`python
import os
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = TelegramClient('bot_session', API_ID, API_HASH)

@bot.on(events.NewMessage(pattern='/start'))
async def handler(event):
    await event.respond('Привет, бот запущен!')

async def main():
    await bot.start(bot_token=BOT_TOKEN)
    print('✅ Бот запущен. Жду команду /start...')
    await bot.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

