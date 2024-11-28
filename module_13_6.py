from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()

# Создаем клавиатуру
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["Рассчитать", "Информация"]
keyboard.add(*buttons)

# Создаем Inline-клавиатуру
inline_keyboard = types.InlineKeyboardMarkup()
inline_buttons = [
    types.InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"),
    types.InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
]
inline_keyboard.add(*inline_buttons)

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.reply('Привет! Я бот, помогающий твоему здоровью. Выберите действие:', reply_markup=keyboard)

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.reply('Выберите опцию:', reply_markup=inline_keyboard)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    formula_text = (
        "Формула Миффлина-Сан Жеора:\n"
        "Для мужчин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (г) + 5\n"
        "Для женщин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (г) - 161"
    )
    await call.message.reply(formula_text)

@dp.callback_query_handler(text='calories')
async def set_gender(call):
    await UserState.gender.set()
    gender_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    gender_buttons = ["Мужчина", "Женщина"]
    gender_keyboard.add(*gender_buttons)
    await call.message.reply('Выберите ваш пол:', reply_markup=gender_keyboard)

@dp.message_handler(state=UserState.gender)
async def set_age(message, state):
    await state.update_data(gender=message.text)
    await UserState.age.set()
    await message.reply('Введите свой возраст:')

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.reply('Введите свой рост:')

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.reply('Введите свой вес:')

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    try:
        gender = data['gender']
        age = int(data['age'])
        growth = int(data['growth'])
        weight = int(data['weight'])

        if gender == "Мужчина":
            # Формула Миффлина - Сан Жеора для мужчин
            calories = 10 * weight + 6.25 * growth - 5 * age + 5
        else:
            # Формула Миффлина - Сан Жеора для женщин
            calories = 10 * weight + 6.25 * growth - 5 * age - 161

        await message.reply(f'Ваша норма калорий: {calories} ккал в день.')
    except ValueError:
        await message.reply('Пожалуйста, введите числовые значения.')
    await state.finish()

@dp.message_handler(text=['Информация'])
async def send_info(message):
    info_text = (
        "Я бот, который помогает вам рассчитать вашу дневную норму калорий. "
        "Для этого мне нужно знать ваш пол, возраст, рост и вес. "
        "Используя формулу Миффлина - Сан Жеора, я вычислю количество калорий, "
        "которое вам нужно потреблять ежедневно для поддержания текущего веса."
    )
    await message.reply(info_text)

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)