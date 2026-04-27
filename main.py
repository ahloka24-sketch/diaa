from telegram import Update, ReplyKeyboardMarkup

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [["نظام الطيبات"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(

        "أهلاً بك في بوت د. ضياء العوضي 👋\nاختر من القائمة:",

        reply_markup=reply_markup

    )

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "نظام الطيبات":

        await update.message.reply_text(

            "📌 نظام الطيبات\n\n"

            "✅ المسموحات:\n"

            "- اللحوم الطبيعية\n"

            "- الخضروات\n"

            "- الفواكه\n"

            "- التمر\n"

            "- العسل الطبيعي\n"

            "- السمن البلدي\n"

            "- اللبن البلدي\n"

            "- الماء\n\n"

            "❌ الممنوعات:\n"

            "- السكر الأبيض\n"

            "- الدقيق الأبيض\n"

            "- الزيوت المهدرجة\n"

            "- المعلبات\n"

            "- المشروبات الغازية\n"

            "- الأطعمة المصنعة\n"

            "- السناكس\n"

            "- الوجبات السريعة"

        )

def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

    print("Bot is running...")

    app.run_polling()

if __name__ == "__main__":

    main()
