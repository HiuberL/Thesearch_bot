from ast import Break
from sqlalchemy import false, true
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
import scrapping
import id
import pickle
import os

def start(context: CallbackContext):    
    filedir = os.path.dirname(os.path.realpath('__file__'))
    for page in id.Datos.page:
        try:
            with open(os.path.join(filedir,'Thesearch_bot\\Data\\'+page +'.txt'), 'rb') as filehandle:
                Data_page = pickle.load(filehandle)
        except:
            Data_page=[]
        DatosP = []
        seguir = true
        for d in id.Datos.Diccionario:
            if seguir:
                Datos = scrapping.scrappingdata(page,d,Data_page)
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
                    DatosP = DatosP+Datos
                else:
                    DatosP = Datos
                if page == 'LIN':
                    seguir = False
                else:
                    seguir = True
                
        if len(DatosP)> 9:
            with open(os.path.join(filedir,'Thesearch_bot\\Data\\'+page +'.txt'), 'wb') as filehandle:
                pickle.dump(DatosP, filehandle)
        else:
            DatosP += Data_page
            with open(os.path.join(filedir,'Thesearch_bot\\Data\\'+page +'.txt'), 'wb') as filehandle:
                pickle.dump(DatosP, filehandle)
            
class comandos(object):

    @staticmethod
    def Agradecimiento(self,update: Update, context: CallbackContext) -> None: 
        update.message.reply_text("Es un placer servirte 😘")

    @staticmethod        
    def Comunicado(update: Update, context: CallbackContext) -> None:
        if update.effective_user.username ==id.Datos.superuser:
            s = " ".join(context.args)
            context.bot.send_message(chat_id=id.Datos.chat_id, text = s, parse_mode='Markdown')    

    @staticmethod        
    def ban(update: Update, context: CallbackContext)-> None:
        if update.effective_user.username == id.Datos.superuser:
            due = context.args[0]        
            context.bot.send_message(chat_id=id.Datos.chat_id,text="No me caes nada bien. El Usuario {} se ha eliminado".format(due))
            context.bot.ban_chat_member(user_id=due, chat_id=id.Datos.chat_id)