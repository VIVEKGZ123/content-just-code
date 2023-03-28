import openai
import logging
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up OpenAI API key
openai.api_key = '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'

# Set up Telegram bot token
TELEGRAM_BOT_TOKEN = '5801244180:AAGiqOifWWREYbtKoVMFFdTS0FKdwHOrGe8'

# Set up logging
logging.basicConfig(level=logging.INFO)

model_id = 'gpt-3.5-turbo'

def format_content(text):
    conversation = [
        {'role': 'system', 'content': 'As the admin of the AI Innovator group, my job is to collect and share the latest news and updates from the AI industry in a way that engages and excites our readers. To achieve this, I have developed a special format style for our WhatsApp posts that includes a captivating headline that grabs the readers attention and piques their curiosity, a brief introduction or summary that provides context and sets the stage for the article, a link to the full article for those who want to read more, and an analysis or commentary from my own perspective that adds value and insight to the article. In addition to these elements, my formatting style also incorporates personalization, emotion, creativity, humor, and contextual understanding to make the content as compelling and memorable as possible. My goal is to create posts that not only inform our readers about the latest AI industry news, but also inspire them and give them goosebumps.Here is the first post that I want you to edit using this formatting style: : :'},
        {'role': 'user', 'content': text}
    ]
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    return response.choices[0].message.content.strip()

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Please send me the AI-related content you want to format.')

def handle_text(update: Update, context: CallbackContext):
    input_text = update.message.text
    formatted_text = format_content(input_text)
    update.message.reply_text(formatted_text, parse_mode=ParseMode.MARKDOWN)

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
