from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "8766723672:AAEGnP1iuj4-nHh9o4I_oPfbhQiSYiZ87Wo"


def get_main_menu():
    keyboard = [
        [KeyboardButton("📝 Register"), KeyboardButton("👩‍💼 Customer Service")],
        [KeyboardButton("ℹ️ What's Trizo")],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "Welcome！Official TRIZO India Support Bot 🇮🇳\n\n"
        "💰 Earn ₹1,000 - ₹5,000 Daily Salary!\n\n"
        "Bhaio, India ka sabse trusted earning platform yahan hai. "
        "Join our VIP Partner program and start your agency today!\n\n"
        "✅ Min Deposit: No Investment: Only keep min ₹200 in bank account\n"
        "✅ Daily Salary: Fixed Income\n"
        "✅ Withdrawal: Instant Bank Transfer\n\n"
        "Please choose👇"
    )

    await update.message.reply_text(
        welcome_text,
        reply_markup=get_main_menu()
    )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📝 Register":
        keyboard = [
            [
                InlineKeyboardButton(
                    "👉 Register Now",
                    url="https://www.trizo.app/register.html?inviteCode=GC20"
                )
            ]
        ]
        await update.message.reply_text(
            "Click below to register:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif text == "👩‍💼 Customer Service":
        keyboard = [
            [
                InlineKeyboardButton(
                    "💬 Contact Support",
                    url="https://t.me/Trizoservice1"
                )
            ]
        ]
        await update.message.reply_text(
            "Click below to contact support:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif text == "ℹ️ What's Trizo":
        await update.message.reply_text(
            "Trizo—Indian best trusted earning platform. 🇮🇳\n\n"
            "Over ten thousand people trade on Trizo everyday. \n"
            "Our secure, user-friendly interface lets you trade anytime, anywhere. \n"
            "Backed by top-tier security and 24/7 support, "
            "we empower you to grow wealth with confidence. \n\n"
            "How Trizo works? 🤔\n\n"
            "1. Finish 5 steps, bind Paytm successfully. ✅\n"
            "2. Keep ₹200-₹10,000 in bank account. 🏦 ₹2,000+ can get more big orders.🚀 \n"
            "3. The system is doing trading automatically with 7×24 hours. 🤖🔄"
        )

    else:
        await update.message.reply_text("Please use the menu.")


def main():
    print("Bot running...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.run_polling()


if __name__ == "__main__":
    main()