import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputFile

TOKEN = "8683122770:AAEUMZjVAbG2Ray3Fv4FHWOK8jn3WLtJrpA"
COMMENT_TEXT = """Не забывайте комментить и ставить реакции, ведь так вы повышаете шанс забрать халявного мишку 🤍

Носителей наших эмодзи и авок частенько радуем подарочками с росписью 🎁"""

# Загружаем фото (InputFile вместо BufferedInputFile - стабильнее)
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
    
    # Пропускаем комментарии
    if message.reply_to_message is not None:
        print(f"⏩ Пропустил комментарий от {message.from_user.first_name}")
        return
    
    full_text = f"""{COMMENT_TEXT}

[Эмодзи]({EMOJI_LINK}) и [авы]({AVATAR_LINK}) — подписывайтесь, чтобы не пропустить раздачи 🎀"""
    
    # Отправляем с фото (если есть) или без
    if PHOTO:
        await message.answer_photo(
            photo=PHOTO,
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
