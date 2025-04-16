from telegram import Update
import os
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Your bot token
BOT_TOKEN = os.getenv("BOT_TOKEN")
# Message to reply with
REPLY_MESSAGE = "@Diaa_Halabi  @Abdalrahmanfarousi  @Mohammad_Mes1999  @MHD_Isam_Almaleh  @Samiabdulfattah  @KaisTawfik  @mohammadkatkout  @YahiaKhaznahKatbi"


# Function that replies when the bot is mentioned
async def reply_if_tagged(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message and message.entities:
        for entity in message.entities:
            if entity.type == "mention":
                mention_text = message.text[entity.offset:entity.offset +
                                            entity.length]
                if mention_text.lower() == f"@{context.bot.username.lower()}":
                    # Determine the correct message thread ID
                    message_thread_id = message.message_thread_id if message.is_topic_message else None

                    # Send the reply, ensuring the thread ID is respected
                    await message.reply_text(
                        REPLY_MESSAGE,
                        message_thread_id=
                        message_thread_id  # Correct thread handling for topics
                    )
                    break


# Set up the bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(
    MessageHandler(filters.TEXT & filters.ChatType.GROUPS, reply_if_tagged))

app.run_polling()
