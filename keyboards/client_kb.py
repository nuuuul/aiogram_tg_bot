from aiogram.types import ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Выбрать город')
b2 = KeyboardButton('/Указать_город')
b3 = KeyboardButton('/Выбрать ценовую категорию')
b4 = KeyboardButton('/DataBase')
b5 = KeyboardButton('/Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b2, b3).row(b4, b5)



ib_back = InlineKeyboardButton(text='назад',
                               callback_data='start')

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like',\
                    callback_data='like_1')).\
                    add(InlineKeyboardButton(text='DisLike',\
                    callback_data='like_1'))



ikb_search = InlineKeyboardMarkup(row_width=2)

ib_city = InlineKeyboardButton(text = 'выбрать город',
                               callback_data= 'city')
ib_activity = InlineKeyboardButton(text = 'выберите активность',
                                   callback_data = 'activity')
ib_price = InlineKeyboardButton(text = 'выберите цену',
                                callback_data='price')

ikb_search.add(ib_city).add(ib_activity).add(ib_price).add(ib_back)




ikb_client_menu = InlineKeyboardMarkup(row_width=2)

ib_search = InlineKeyboardButton(text = 'Поиск 🔍',
                                 callback_data='search')
ib_db = InlineKeyboardButton(text = 'Каталог 🛒',
                             callback_data='db')
ib_links = InlineKeyboardButton(text = 'Ссылки',
                                callback_data='links')
ib_description = InlineKeyboardButton(text = 'Описание',
                                      callback_data='description')
ib_start = InlineKeyboardButton(text = 'Перезапустить бота',
                                callback_data= 'start')
ib_openkb = InlineKeyboardButton(text = 'Открыть клавиатуру',
                                 callback_data= 'kb_open')

ikb_client_menu.row(ib_search, ib_db).row(ib_links, ib_description).add(ib_openkb).add(ib_start)




ikb_links = InlineKeyboardMarkup(row_width=1)
ib_tg = InlineKeyboardButton(text = 'telegram', url = 'https://t.me/dddodik')
ib_fl = InlineKeyboardButton(text = 'FL.ru', url = 'https://www.fl.ru/users/bugagashenkashe/portfolio/')
ib_gh = InlineKeyboardButton(text = 'GitHub', url = 'https://github.com/nuuuul')
ikb_links.add(ib_tg).add(ib_fl).add(ib_gh).add(ib_back)



ikb_back = InlineKeyboardMarkup(row_width=1)
ikb_back.add(ib_back)
