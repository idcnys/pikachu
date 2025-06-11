from typing import Final

# pip install python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

print('Starting up bot...')

TOKEN: Final = '7925285512:AAG1R_MEsyxCqbC_0zQJSXwPJXcb-ATc8To'
BOT_USERNAME: Final = '@cse_c_bot'


# Lets us use the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m pikachu known as pika pika your section assistant. How can i help you today? Enter /help to know every command i can help you with <3.')


# Lets us use the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('/routine will provide you with the latest updated routine.\n /ct will provide you with the CT schedule.\n/today will show you today\'s routine\n /latest will try to inform you if any information is available or not.')


# Lets us use the /custom command
async def routine_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('[Live routine link](https://routine-c.vercel.app) Pika pika I\'m working on it... please wait few days :)')
async def today_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Have a great day \nPika pika I\'m working on it... please wait few days :)')
async def latest_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Sumon & Rabbi will tell you. Pika pika I\'m working on it... please wait few days :)')
async def ct_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Pika pika I\'m working on it... please wait :)')


def handle_response(text: str) -> str:
    # Create your own response logic
    psd: str = text.lower()

    if 'hello' in psd:
        return 'Hi, pika pika pikachuuu...'

    if 'how are you' in psd:
        return 'I\'m good! how are you???'

    if 'thanks' in psd:
        return 'Pikaa pikaa xD'
    if 'sorry' in psd and 'bol' in psd:
        return 'I am sorry :('
        

    return 'Pika pikaaa. I don\'t understand. It is not programmed yet. Please wait'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return  # We don't want the bot respond if it's not mentioned in the group
    else:
        response: str = handle_response(text)

    # Reply normal if the message is in private
    print('Bot:', response)
    await update.message.reply_text(response)


# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('routine', routine_command))
    app.add_handler(CommandHandler('ct', ct_command))
    app.add_handler(CommandHandler('today', today_command))
    app.add_handler(CommandHandler('latest', latest_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    app.add_error_handler(error)

    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)

