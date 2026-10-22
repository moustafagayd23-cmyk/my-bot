from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
import io

TOKEN = "8986668699:AAGTBKN8d2c1lA07NbTOexkSibRQfY_E53A"

async def start(update, context):
    await update.message.reply_text("بوت مصطفى شغال 24 ساعة! ابعت صورتك")

async def handle_photo(update, context):
    file = await update.message.photo[-1].get_file()
    b = await file.download_as_bytearray()
    context.user_data['photo'] = bytes(b)
    kb = [[InlineKeyboardButton("كاجوال رجالي", callback_data="a")],[InlineKeyboardButton("كاجوال حريمي", callback_data="b")]]
    await update.message.reply_text("اختار:", reply_markup=InlineKeyboardMarkup(kb))

async def button_click(update, context):
    q = update.callback_query
    await q.answer()
    await q.edit_message_text("تم")
    await q.message.reply_photo(photo=io.BytesIO(context.user_data['photo']))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
app.add_handler(CallbackQueryHandler(button_click))
app.run_polling()
