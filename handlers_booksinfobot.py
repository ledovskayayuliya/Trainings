import requests
from main import bot, dp
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.storage import FSMContext
from config import key


async def send_to_admin(*args):
    try:
        await bot.send_message(chat_id='345217091', text="Bot is started")
    except:
        pass


@dp.message_handler(commands=['start'])
async def process_start_command(message: Message, state: FSMContext):
    await message.answer('Hello! I can help you to find any book. Just send me the title')


@dp.message_handler(content_types=['text'])
async def book_send(message: Message):
    if message.text:
        name_book = message.text
        url = f'https://www.googleapis.com/books/v1/volumes?q={name_book}&key={key}'
        answer = requests.get(url)
        answer = answer.json().get('items')
        for i in answer:

            title = i.get('volumeInfo').get('title')
            authors = i.get('volumeInfo').get('authors')
            previewLink = i.get('volumeInfo').get('previewLink')
            description = i.get('volumeInfo').get('description')
            if not description:
                description = 'нет описания'
            publishedDate = i.get('volumeInfo').get('publishedDate')
            inline_kb_full = InlineKeyboardMarkup(row_width=2)
            btn = InlineKeyboardButton('Посмотреть', url=previewLink)
            inline_kb_full.add(btn)
            text = f'Название произведения:{title}\n\nАвтор:{authors}\n\nДата публикации:{publishedDate}\n\nОписание:{description}'
            await message.answer(text, reply_markup=inline_kb_full)
