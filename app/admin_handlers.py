from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon_ru import LEXICON_RU

# Инициализируем роутер уровня модуля
admin = Router()
