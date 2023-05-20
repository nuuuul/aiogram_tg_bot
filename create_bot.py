from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

storage = MemoryStorage()

bot = Bot(token= '5642912391:AAHz98XGu_VPi5oN8DSHeLqXqq8QYj84ve4')
dp = Dispatcher(bot, storage=storage)