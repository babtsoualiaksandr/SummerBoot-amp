#!python3
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""

Usage:

Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import re
import configparser

from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, Filters, MessageHandler, Updater

from game_gallow import get_random_word as get_word


config = configparser.ConfigParser()
config.read("settings.ini")


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

game_on = False

word_sought: str
word_unknown: str
error = 0
errors_max = 10


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    menu_main = [[InlineKeyboardButton('To start playing ', callback_data='start_game_gallows')],
                 [InlineKeyboardButton('Not!! Better to learn Python', callback_data='exit')], ]
    reply_markup = InlineKeyboardMarkup(menu_main)
    update.message.reply_text(
        f' {user.first_name} Pls choose the option:', reply_markup=reply_markup)


def menu_actions(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    global game_on, word_sought, word_unknown, error
    if query.data == 'start_game_gallows':
        game_on = True
        word_sought = get_word()
        word_unknown = '-' * len(word_sought)
        error = 0
        update.callback_query.message.edit_text(
            f"{update.effective_user.first_name} Let's start playing!!! Guess the word  {word_unknown}?")

    if query.data == 'exit':
        game_on = False
        msg = '\U0001F916 \U0001F300  \U0001F601 \U0001F60D\n'
        update.callback_query.message.edit_text(
            f'{update.effective_user.first_name} {msg} Goodbye, do a better job')



def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help Ouuu!')


def exit_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /exit is issued."""
    update.message.reply_text('Exit')


def echo(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    print('chat_id = @@@@@@@@@@@@@@@@@@@@@@',chat_id)
    global game_on, word_sought, word_unknown, error, errors_max
    if game_on == True:
        if (not len(update.message.text) == 1) | update.message.text.isdigit():
            update.message.reply_text(
                f'Error input... <{update.message.text}> pls ONE letter ')
        if error == errors_max+1:
            msg = '\U0001F614'
            update.message.reply_text(
                f"You didn't guess the word <{word_sought}> <{word_unknown}> {msg}")
            game_on = False
        elif (error < errors_max+1) & (not word_unknown == word_sought):
            input_letter = update.message.text.lower()
            indexes_find = [m.start()
                            for m in re.finditer(input_letter, word_sought)]
            if len(indexes_find) == 0:
                error += 1
                update.message.reply_text(
                    f'There is no such letter {update.message.text} in the word {word_unknown} Attempts left {errors_max+1-error}')
            else:
                list_word_unknown = list(word_unknown)
                for idx in indexes_find:
                    list_word_unknown[idx] = input_letter
                word_unknown = "".join(list_word_unknown)
                update.message.reply_text(
                    f'There is such a letter!!!  {word_unknown}')
                if word_unknown == word_sought:
                    update.message.reply_text(
                        f'Congratulations, you guessed the word <{word_unknown}>')                    
                    game_on = False

    else:
        update.message.reply_text(
            "You don't want to work but want to play? decide click /start")


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    print(config["Telegram"]["token"])
    updater = Updater(
        config["Telegram"]["token"], use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("exit", exit_command))

    dispatcher.add_handler(CallbackQueryHandler(menu_actions))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
