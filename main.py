from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

import os

TOKEN = os.getenv("8222275804:AAGXdVkVJjxQ4yPvKK5Cyhde_Y7gqSLTwfo")   # 🔑 Render me environment variable set karenge

CHANNELS = ["@myproteam", "@BHAIKITEAM0", "@BHAIKITEAMCHAT"]

def check_membership(bot, user_id):
    for channel in CHANNELS:
        try:
            member = bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        except:
            return False
    return True

def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if check_membership(context.bot, user_id):
        keyboard = [
            [InlineKeyboardButton("🎁 Refer & Earn", callback_data="refer")],
            [InlineKeyboardButton("💸 Withdraw", callback_data="withdraw")]
        ]
        update.message.reply_text(
            "✅ Welcome! You have joined all channels.\nChoose an option:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        update.message.reply_text(
            "⚠️ Please join all required channels first:\n\n"
            "👉 @YourChannel1\n👉 @YourChannel2\n👉 @YourChannel3\n\n"
            "Then type /start again ✅"
        )

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "refer":
        query.edit_message_text(
            text="🎁 Your Refer Link:\nhttps://t.me/MyProTeamBot?start=" + str(query.from_user.id)
        )
    elif query.data == "withdraw":
        query.edit_message_text("💸 Withdraw system coming soon...")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()