#!python3


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


from game_gallow import GameGallow
from game_gallow import letter_from_player


config = configparser.ConfigParser()
config.read("settings.ini")


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


players_games = {}


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
    global players_games
    chat_id = update.effective_user.id
    if query.data == 'start_game_gallows':
        players_games[chat_id] = GameGallow()
        update.callback_query.message.edit_text(
            f"{update.effective_user.first_name} Let's start playing! Guess the word {players_games[chat_id].word_unknown}?")
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
    global players_games

    if update.effective_user.id in players_games:
        players_games.pop(update.effective_user.id)

    update.message.reply_text(
        f'Delete id = {update.effective_user.id} and Exit')


def stat_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /stat is issued."""
    global players_games
    msg = '\U0001F300 \n'
    for key in players_games:
        msg += f'Player: {key} \U0001F60D\n'
        print(players_games[key])
        msg += str(players_games[key])
    update.message.reply_text(f'Stat game {msg}\n')


def game_gallow(update: Update, context: CallbackContext) -> None:
    global players_games
    chat_id = update.message.chat_id
    update.message.reply_text(letter_from_player(
        chat_id, update.message.text, players_games))


def main() -> None:
    updater = Updater(
        config["Telegram"]["token"], use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("exit", exit_command))
    dispatcher.add_handler(CommandHandler("stat", stat_command))
    dispatcher.add_handler(CallbackQueryHandler(menu_actions))
    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, game_gallow))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
