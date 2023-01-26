from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp,db
from utils.db_api.sqlite import *
from aiogram.types import CallbackQuery
from  keyboards.inline.lang import laguage, laguageen, laguageru, laguagetk, laguageuz
#DAsturchi : @MrGayratov
#MAnba : @KingsOfPy
langa = f"<b>🌍 Choose a Language :</b>"

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        db.add_lang(id=message.from_user.id,
                    )
    except sqlite3.IntegrityError as err:
        pass
    id =message.chat.id
    lang = db.select_lang(id=id)
    if lang[1] == 'uz':
        await message.answer(f"<b>🌍 Choose a Language :</b>",reply_markup=laguage)
    if lang[1] == 'eng':
        await message.answer("<b>Hello! You can download videos from Instagram, Tik-Tok, through this bot.\n\nSend the video link you want to download:</b> <i>(Maximum video upload size is 20mb)</i>")
    if lang[1] == 'rus':
        await message.answer("<b>Привет, через этого бота можно скачивать видео из Instagram, Tik-Tok.\n\nОтправьте ссылку на видео, которое хотите скачать:</b> <i>(Максимальный размер загружаемого видео 20 МБ.</i>)")
    if lang[1] == 'uzb':
        await message.answer("<b>Assalomu Alaykum, ushbu bot orqali Instagram va Tik-Tokdan videolarni yuklab olishingiz mumkin.\n\nYuklash kerak bo'lgan video havolasini (linkini) yuboring:</b> <i>(Maksimal video yuklash hajmi 20mb)</i>")
    if lang[1] == 'turk':
        await message.answer("<b>Merhaba! Bu bot aracılığıyla Instagram, Tik-Tok'tan video indirebilirsiniz.\n\nİndirmek istediğiniz video bağlantısını gönderin:</b> <i>(Maksimum video yükleme boyutu 20mb'dir)</i>")

    @dp.callback_query_handler(text="rus")
    async def bot_echo(call: CallbackQuery):
        await call.message.edit_text(langa, reply_markup=laguageru)
        callback_data = call.data
        try:
            db.update_user_lang(id=call.from_user.id,
                                lang=callback_data)

            id = call.message.chat.id
            lang = db.select_lang(id=id)
            if lang[1] == 'rus':
                await call.answer("🇷🇺 Язык успешно изменен")
                await call.answer(cache_time=60)
        except sqlite3.IntegrityError as err:
            pass

    @dp.callback_query_handler(text="eng")
    async def bot_echo(call: CallbackQuery):
        await call.message.edit_text(langa, reply_markup=laguageen)
        callback_data = call.data
        try:
            db.update_user_lang(id=call.from_user.id,
                                lang=callback_data)

            id = call.message.chat.id
            lang = db.select_lang(id=id)
            if lang[1] == 'eng':
                await call.answer("🇬🇧 Laguage changed  successfully")
                await call.answer(cache_time=60)
        except sqlite3.IntegrityError as err:
            pass
    @dp.callback_query_handler(text="uzb")
    async def bot_echo(call: CallbackQuery):
        await call.message.edit_text(langa, reply_markup=laguageuz)
        callback_data = call.data
        try:
            db.update_user_lang(id=call.from_user.id,
                                lang=callback_data)

            id = call.message.chat.id
            lang = db.select_lang(id=id)
            if lang[1] == 'uzb':
                await call.answer("🇺🇿 Til muvaffaqiyatli o'zgartirildi")
                await call.answer(cache_time=60)
        except sqlite3.IntegrityError as err:
            pass
    @dp.callback_query_handler(text="turk")
    async def bot_echo(call: CallbackQuery):
        await call.message.edit_text(langa, reply_markup=laguagetk)
        callback_data = call.data
        try:
            db.update_user_lang(id=call.from_user.id,
                                lang=callback_data)

            id = call.message.chat.id
            lang = db.select_lang(id=id)
            if lang[1] == 'turk':
                await call.answer("🇹🇷 Dil başarıyla değiştirildi")
                await call.answer(cache_time=60)
        except sqlite3.IntegrityError as err:
            pass

@dp.message_handler(commands='lang')
async def bot_start(message: types.Message):
    id = message.chat.id
    lang =db.select_lang(id=id)
    if lang[1] == 'eng':
        await message.answer(langa,reply_markup=laguageen)
    if lang[1] == 'rus':
        await message.answer(langa,reply_markup=laguageru)
    if lang[1] == 'uzb':
        await message.answer(langa,reply_markup=laguageuz)
    if lang[1] == 'turk':
        await message.answer(langa,reply_markup=laguagetk)

@dp.message_handler(commands='hello')
async def bot_hello(message: types.Message):
    id = message.chat.id
    lang =db.select_lang(id=id)
    if lang[1] == 'eng':
        await message.answer('hello')
    if lang[1] == 'rus':
        await message.answer('Privet')
    if lang[1] == 'uzb':
        await message.answer('salom')
    if lang[1] == 'turk':
        await message.answer('Merhaba')
