from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command

from parser.kinjki import par, par_new
from filters.chat_types import ChatTypeFilter
from kbbs import reply

hud_url = "https://www.bookcity.kz/khudozhestvennaya-literatura-66108/"
classik_url = "https://www.bookcity.kz/klassicheskaya-literatura-66109/"
socrem_url = "https://www.bookcity.kz/sovremennaya-literatura-66114/"
ostro_url = "https://www.bookcity.kz/ostrosyuzhetnaya-literatura-66118/"
poezia_url = "https://www.bookcity.kz/poeziya-66119/"
foreign_url  = "https://www.bookcity.kz/foreign-books-66120/"



user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет, здесь ты можешь выбрать любую книгу на свой вкус)", reply_markup=reply.start_kb)

@user_private_router.message(Command('menu'))# можно еще импортировать функцию or_f с filters это аналог or: or_f((Command()), (F...))
async def menu_cmd(message: types.Message):
    await message.answer(message.text)#инлайн кнопки

@user_private_router.message(Command('top_25'))
async def top_cmd(message: types.Message):
    await message.answer(message.text)

@user_private_router.message(Command('new'))
async def new_cmd(message: types.Message):
    spisok = par_new(url=hud_url)
    for i in spisok.keys():
        await message.answer(f'''name: {spisok[i]["name"]} 
price: {spisok[i]["price"]}''')

@user_private_router.message(Command('about_us'))
async def about_cmd(message: types.Message):
    await message.answer(message.text)

# @user_private_router.message(F.text.lower() == 'Контакты разработчиков') # можно засунуть операторы такие как "или" -- |, "и" -- &: F... | F...
# async def aboba_cmd(message: types.Message):
#     await message.answer('Маг фильтр')


# Если не хочешь чтобы твоего бота добавляли в другие группы
# В BotFather заходишь в BotSettings
# Потом в Allow Groups Turn groups off