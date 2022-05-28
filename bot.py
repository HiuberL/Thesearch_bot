import logging
import scrapping
import telegram
from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import numpy as np
import id
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
DatosCT = []
DatosUME = []
DatosLin = []
    
def Agradecimiento(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Es un placer servirte 😘")
    
def start(context: CallbackContext)-> None:
    global DatosCT, DatosUME, DatosLin
    DatosP = []
    for d in id.Diccionario:
        Datos = scrapping.scrappingComputrabajo(d,DatosCT)
        for n in range(0,len(Datos)):
            Descripcion = str(Datos[n][2])
            Descripcion = Descripcion.replace("\n\n", "\n")
            Descripcion = Descripcion.replace("*",' ')
            keyboard = InlineKeyboardMarkup.from_button(InlineKeyboardButton(text="Más Información", url=Datos[n][3]))       
            try:
                context.bot.send_message(chat_id=id.Datos.chat_id,text="🔴 *"+Datos[n][0]+"*🔴\n▶️_"+Datos[n][1]+"_ ◀️\n \n*Descripción*:\n"+Descripcion+"\n" , parse_mode='Markdown',reply_markup=keyboard)
            except:
                pass
        if len(DatosP)!=0:
            DatosP = DatosP+ Datos
        else:
            DatosP = Datos
    if len(DatosP)> 0:
        DatosCT = DatosP
    DatosP = []
    for d in id.Diccionario:
        Datos = scrapping.scrappingUnmejorempleo(d,DatosUME)
        for n in range(0,len(Datos)):
            Descripcion = str(Datos[n][2])
            Descripcion = Descripcion.replace("\n\n", "\n")
            Descripcion = Descripcion.replace("*",' ')
            keyboard = InlineKeyboardMarkup.from_button(InlineKeyboardButton(text="Más Información", url=Datos[n][3]))       
            try:
                context.bot.send_message(chat_id=id.Datos.chat_id,text="🔴 *"+Datos[n][0]+"*🔴\n▶️_"+Datos[n][1]+"_ ◀️\n \n*Descripción*:\n"+Descripcion+"\n" , parse_mode='Markdown',reply_markup=keyboard)
            except:
                pass
        if len(DatosP)!=0:
            DatosP = DatosP + Datos
        else:
            DatosP = Datos
    if len(Datos)> 0:
        DatosUME = DatosP
    DatosP = []    
    Datos = scrapping.scrappinglinkedin(DatosLin)
    for n in range(0,len(Datos)):
        Descripcion = str(Datos[n][2])
        Descripcion = Descripcion.replace("\n\n", "\n")
        Descripcion = Descripcion.replace("*",' ')
        keyboard = InlineKeyboardMarkup.from_button(InlineKeyboardButton(text="Más Información", url=Datos[n][3]))       
        try:
            if Datos[n][0]!="":
                context.bot.send_message(chat_id=id.Datos.chat_id,text="🔴 *"+Datos[n][0]+"*🔴\n▶️_"+Datos[n][1]+"_ ◀️\n \n*Descripción*:\n"+Descripcion+"\n" , parse_mode='Markdown',reply_markup=keyboard)
        except:
            pass
    if len(DatosP)!=0:
        DatosP = DatosP + Datos 
    else:
        DatosP = Datos
    if len(Datos)> 0:
        DatosLin = DatosP
def Comunicado(update: Update, context: CallbackContext) -> None:
    if update.effective_user.username =="KlHiuber":
        s = " ".join(context.args)
        context.bot.send_message(chat_id=id.Datos.chat_id, text = s, parse_mode='Markdown')    

def ban(update: Update, context: CallbackContext)-> None:
    if update.effective_user.username =="KlHiuber":
        due = context.args[0]        
        context.bot.send_message(chat_id=id.Datos.chat_id,text="No me caes nada bien. El Usuario {} se ha eliminado".format(due))
        context.bot.ban_chat_member(user_id=due, chat_id=id.Datos.chat_id)
    
def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(id.Datos.Token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    
    # on different commands - answer in Telegram
    j = updater.job_queue
    j.run_once(start,0.1)
    j.run_repeating(start,14400)
    dispatcher.add_handler(CommandHandler("comunicado", Comunicado))
    dispatcher.add_handler(CommandHandler("Ban_Camila", ban))
    dispatcher.add_handler(CommandHandler("Gracias", Agradecimiento))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
