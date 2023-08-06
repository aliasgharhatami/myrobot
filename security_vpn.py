import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
BOT_TOKEN = '6050758289:AAGQGgnJqsq0DGhLX56MseOFlw2WtHLa9Y4'

# Lists
list_1 = ["proton", "psiphon", "v2ray", "v2rayng", "outline", "tor", "ourbot"]
list_2 = ["argo"]

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Welcome message with the Start button
welcome_message = (".برای شروع دکمه استارت را در پایین بزنید.اگر در انتها فکر میکنید اشتباهی پیش آمده به آدرس زیر ایمیل بزنید: test_vpn_security.bot@proton.me")

# Start command handler
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message.from_user.id
    # Create a Start button
    start_button = KeyboardButton('Start')
    keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(start_button)

    await message.reply(welcome_message, reply_markup=keyboard_markup)


# Message handler for receiving user's name
@dp.message_handler(lambda message: message.text == 'Start', content_types=types.ContentTypes.TEXT)
async def ask_name(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(user_id, "اسم وی پی ان خود را به انگلیسی وارد نمایید:")


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_name(message: types.Message):
    user_id = message.from_user.id
    user_input = message.text.replace("vpn" , "").strip().lower()

    if user_input in list_1:
        await bot.send_message(user_id, " .وی پی ان شما امن است.همیشه از وی پی ان های معتبر استفاده نمایید.میخواهید نام دیگری هم امتحان کنید؟ ")
    elif user_input in list_2:
        await bot.send_message(user_id, " امن نیست!!!.لطفا برای امنیت خودتان از وی پی ان های امن استفاده کنید و آن را از منابع معتبر دانلود نمایید.میخواهید نام دیگری هم امتحان کنید؟.")
    else:
        await bot.send_message(user_id, ".این وی پی ان برای ما ثبت نشده است.در حال حاضر اطلاعی از آن نداریم.میخواهید نام دیگری هم امتحان کنید؟")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
