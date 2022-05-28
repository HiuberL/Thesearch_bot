from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
import scrapping
import id

class comandos():
    def __init__(self) -> None:        
        self.DatosCT = []
        self.DatosUME = []
        self.DatosLin = []
    
    @staticmethod
    def Agradecimiento(update: Update, context: CallbackContext) -> None:
        update.message.reply_text("Es un placer servirte 😘")

    @staticmethod        
    def Comunicado(update: Update, context: CallbackContext) -> None:
        if update.effective_user.username =="KlHiuber":
            s = " ".join(context.args)
            context.bot.send_message(chat_id=id.Datos.chat_id, text = s, parse_mode='Markdown')    

    @staticmethod        
    def ban(update: Update, context: CallbackContext)-> None:
        if update.effective_user.username =="KlHiuber":
            due = context.args[0]        
            context.bot.send_message(chat_id=id.Datos.chat_id,text="No me caes nada bien. El Usuario {} se ha eliminado".format(due))
            context.bot.ban_chat_member(user_id=due, chat_id=id.Datos.chat_id)

    @classmethod
    def start(self,context: CallbackContext)-> None:
        DatosP = []
        for d in id.Diccionario:
            Datos = scrapping.scrappingComputrabajo(d,self.DatosCT)
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
            self.DatosCT = DatosP
        DatosP = []
        for d in id.Diccionario:
            Datos = scrapping.scrappingUnmejorempleo(d,self.DatosUME)
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
                self.DatosP = DatosP + Datos
            else:
                DatosP = Datos
        if len(Datos)> 0:
            DatosUME = DatosP
        DatosP = []    
        Datos = scrapping.scrappinglinkedin(self.DatosLin)
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
            self.DatosLin = DatosP

