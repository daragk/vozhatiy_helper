from aiogram import types, F, Router
from aiogram.filters.command import Command

import interact_with_gamedatabase
import kboards

router = Router()


@router.message(Command('start'))
async def start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Игры")],
        [types.KeyboardButton(text="Меро")],
        [types.KeyboardButton(text="Свечки")],
        [types.KeyboardButton(text="НиП", resize_keyboard=True)]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"Приветствую, {message.from_user.full_name}!")
    await message.answer("Need help with...?", reply_markup=keyboard)


@router.message(F.text == 'Меро')
async def lol(message: types.Message):
    await message.answer('тут будет предложено выбрать категорию')


@router.message(F.text == 'Свечки')
async def lol(message: types.Message):
    await message.answer('тут будет предложено выбрать категорию')


@router.message(F.text == 'Игры')
async def games_categories(message: types.Message):
    ikb = [
        [types.KeyboardButton(text="На знакомство", resize_keyboard=True)],
        [types.KeyboardButton(text="Выявление лидера", resize_keyboard=True)],
        [types.KeyboardButton(text="Игры-минутки", resize_keyboard=True)],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=ikb)
    await message.answer('выбрать категорию', reply_markup=keyboard)


@router.message(F.text == 'Игры-минутки')
async def igri_minutki(message: types.Message):
    await message.answer(interact_with_gamedatabase.get_igra_minutka())


@router.message(F.text == 'Выявление лидера')
async def games_start(message: types.Message):
    await message.answer(interact_with_gamedatabase.get_igra_na_lidera())


@router.message(F.text == 'На знакомство')
async def games_start(message: types.Message):
    await message.answer(interact_with_gamedatabase.get_igra_na_znakomstvo())


@router.message(F.text == 'НиП')
async def games_start(message: types.Message):
    await message.answer('Н или П?', reply_markup=kboards.get_nip_kb())


@router.message(F.text == 'Наказания')
async def games_start(message: types.Message):
    await message.answer(interact_with_gamedatabase.nip_nakazaniya())


@router.message(F.text == 'Поощрения')
async def games_start(message: types.Message):
    await message.answer(interact_with_gamedatabase.nip_pooschreniya())
