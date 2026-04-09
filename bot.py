import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8683122770:AAEUMZjVAbG2Ray3Fv4FHWOK8jn3WLtJrpA"
COMMENT_TEXT = """Не забывайте комментить и ставить реакции, ведь так вы повышаете шанс забрать халявного мишку 🤍

Носителей наших эмодзи и авок частенько радуем подарочками с росписью 🎁 (+ повышенный приз)"""

bot = Bot(token=TOKEN)
dp = Dispatcher()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎁 Наши эмодзи", url="https://t.me/addemoji/DOSIK_emoji")],
    [InlineKeyboardButton(text="⭐ Звезды от Досика", url="https://t.me/Dosik_stars_bot")],
    [InlineKeyboardButton(text="📺 Наш твич", url="https://www.twitch.tv/")],
    [InlineKeyboardButton(text="💬 Наш чатик", url="https://t.me/chatik_DOSIK")],
])

@dp.message()
async def handle_message(message: types.Message):
    # Проверяем, что сообщение отправлено каналом (а не пользователем)
    if message.sender_chat and message.sender_chat.type == "channel":
        print(f"Пост из канала в чате обсуждения, отвечаем")
        await message.reply(COMMENT_TEXT, reply_markup=keyboard)
    else:
        print("Обычное сообщение от пользователя, игнорируем")

async def main():
    print("🚀 Бот запущен!")
    print("📢 Отвечает на сообщения канала в чате обсуждения")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
