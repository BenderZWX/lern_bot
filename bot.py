from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def greet_user(bot, update):
    text = 'Ввели /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text) #Форматирование строки, подставляет данные в скобочки 
                                                                                                        #(Первые скобочки имя: Воторые сам текст)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.first_name, 
                 update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    dp = mybot.dispatcher #принимает входящие и распределяет по получателям (CommandHandler и тд)
    dp.add_handler(CommandHandler('start', greet_user)) #greet_user название функции может называться хоть как
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot is started")
    
    mybot.start_polling()
    mybot.idle()

main()