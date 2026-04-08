import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import BufferedInputFile

TOKEN = "8683122770:AAEUMZjVAbG2Ray3Fv4FHWOK8jn3WLtJrpA"
COMMENT_TEXT = """Не забывайте комментить и ставить реакции, ведь так вы повышаете шанс забрать халявного мишку 🤍

Носителей наших эмодзи и авок частенько радуем подарочками с росписью 🎁"""

# Загружаем фото
try:
    with open("image.jpg", "rb") as photo_file:
        PHOTO_BYTES = photo_file.read()
    PHOTO_INPUT = BufferedInputFile(PHOTO_BYTES, filename="image.jpg")
    print("✅ Фото успешно загружено")
except FileNotFoundError:
    print("❌ Ошибка: файл image.jpg не найден!")
    PHOTO_INPUT = None

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Кнопки
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎁 Повышенный приз", url="https://t.me/DosikGIFTS/11423")],
    [InlineKeyboardButton(text="⭐ Звезды от Досика", url="https://t.me/Dosik_stars_bot")],
    [InlineKeyboardButton(text="📺 Наш твич", url="https://www.twitch.tv/")],
    [InlineKeyboardButton(text="💬 Наш чатик", url="https://t.me/chatik_DOSIK")],
])

EMOJI_LINK = "https://t.me/addemoji/DOSIK_emoji"
AVATAR_LINK = "https://t.me/EMOJI_DOSIK"

@dp.message()
async def auto_comment(message: types.Message):
    # Не отвечаем сами себе
    if message.from_user.id == bot.id:
        return
    
    # Пропускаем комментарии (ответы на другие сообщения)
    if message.reply_to_message is not None:
        print(f"⏩ Пропустил комментарий от {message.from_user.first_name}")
        return
    
    full_text = f"""{COMMENT_TEXT}

[Эмодзи]({EMOJI_LINK}) и [авы]({AVATAR_LINK}) — подписывайтесь, чтобы не пропустить раздачи 🎀"""
    
    # Отправляем фото в чат (НЕ ответом на сообщение)
    if PHOTO_INPUT:
        await message.answer_photo(  # <-- ИСПРАВЛЕНО: answer_photo вместо reply_photo
            photo=PHOTO_INPUT,
            caption=full_text,
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    else:
        await message.answer(
            full_text,
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    print(f"✅ Ответил на пост от {message.from_user.first_name}")

async def main():
    print("🚀 Бот запущен!")
    print("📢 Отвечает только на новые посты (игнорирует комментарии)")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
