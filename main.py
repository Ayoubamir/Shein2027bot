from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8917269579:AAGKVjNLvx-pgTmj08vjpx2PvNsjl3BesYw"

LINK = "https://onelink.shein.com/40/5u7suqhacwzm"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🇫🇷 France 60%", url=LINK),
            InlineKeyboardButton("🇪🇸 Spain 60%", url=LINK),
        ],
        [
            InlineKeyboardButton("🇮🇹 Italy 60%", url=LINK),
            InlineKeyboardButton("🇩🇪 Germany 60%", url=LINK),
        ]
    ]

    await update.message.reply_text(
        "Please select your country to get your 60% SHEIN coupon:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
