from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon_ru import LEXICON_RU
from app.states import Chat
from aiogram.fsm.context import FSMContext
from app.gpt import gpt_text
import app.keyboards as kb

# Инициализируем роутер уровня модуля
user = Router()


@user.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=kb.main)


@user.message(F.text == 'Чат c ИИ')
async def chatting(message: Message, state: FSMContext):
    await state.set_state(Chat.text)
    await message.answer("Введите Ваш запрос")


@user.message(Chat.text)
async def chat_response(message: Message, state: FSMContext):
    response = await gpt_text(message.text, 'gpt-4o-mini')
    await message.answer(response)


@user.message()
async def answer_to_text(message: Message):
    await message.answer("Чтобы задать вопрос к ИИ, воспользуйтесь кнопкой 'Чат с ИИ'")
