import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8683122770:AAEUMZjVAbG2Ray3Fv4FHWOK8jn3WLtJrpA"
COMMENT_TEXT = """Не забывайте комментить и ставить реакции, ведь так вы повышаете шанс забрать халявного мишку 🤍

Носителей наших эмодзи и авок частенько радуем подарочками с росписью 🎁 (+ повышенный приз)"""

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Кнопки
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎁 Наши эмодзи", url="https://t.me/addemoji/DOSIK_emoji")],
    [InlineKeyboardButton(text="⭐ Звезды от Досика", url="https://t.me/Dosik_stars_bot")],
    [InlineKeyboardButton(text="📺 Наш твич", url="https://www.twitch.tv/")],
    [InlineKeyboardButton(text="💬 Наш чатик", url="https://t.me/chatik_DOSIK")],
])

@dp.channel_post()
async def auto_comment(message: types.Message):
    if message.reply_to_message is not None:
        print(f"⏩ Пропустил комментарий (ответ)")
        return
    
    await message.reply(
        COMMENT_TEXT,
        reply_markup=keyboard
    )
    print(f"✅ Ответил комментарием на пост в канале")

async def main():
    print("🚀 Бот запущен!")
    print("📢 Отвечает комментарием под каждым новым постом в КАНАЛЕ")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
