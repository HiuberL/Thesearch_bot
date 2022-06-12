import logging
import telegram
from telegram.ext import Updater, CommandHandler
import numpy as np
import commands
import id
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    updater = Updater(id.Datos.Token)

    dispatcher = updater.dispatcher
    comandos = commands.comandos()
    j = updater.job_queue
    j.run_once(commands.start,0.1)
    j.run_once(commands.start,7200)
    dispatcher.add_handler(CommandHandler("comunicado", comandos.Comunicado))
    dispatcher.add_handler(CommandHandler("Ban_Camila", comandos.ban))
    dispatcher.add_handler(CommandHandler("Gracias", comandos.Agradecimiento))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
