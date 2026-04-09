import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputFile

TOKEN = "8683122770:AAEUMZjVAbG2Ray3Fv4FHWOK8jn3WLtJrpA"
COMMENT_TEXT = """Не забывайте комментить и ставить реакции, ведь так вы повышаете шанс забрать халявного мишку 🤍

Носителей наших эмодзи и авок частенько радуем подарочками с росписью 🎁 (+ повышенный приз)"""

# Фото (файл image.jpg должен быть в репозитории)
try:
    PHOTO = InputFile("image.jpg")
    print("✅ Фото успешно загружено")
except Exception as e:
    print(f"❌ Ошибка загрузки фото: {e}")
    PHOTO = None

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
    # Пропускаем комментарии (ответы на другие сообщения)
    if message.reply_to_message is not None:
        print(f"⏩ Пропустил комментарий (ответ)")
        return
    
    if PHOTO:
        await message.answer_photo(
            photo=PHOTO,
            caption=COMMENT_TEXT,
            reply_markup=keyboard  # <-- убрал parse_mode
        )
    else:
        await message.answer(
            COMMENT_TEXT,
            reply_markup=keyboard  # <-- убрал parse_mode
        )
    print(f"✅ Ответил на пост в канале")

async def main():
    print("🚀 Бот запущен!")
    print("📢 Отвечает только на новые посты в КАНАЛЕ")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
