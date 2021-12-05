import telebot
token='5044543751:AAHrrI0S9RfpHWfWj37fbm6oEptQWlDH3kA'
bot=telebot.TeleBot(token)
class PhoneContact():
    def __init__(self):
        self.Nambers={}
    def appendContact(self,Name,Number):
        self.Nambers[Name]=Number
        print(self.Nambers)
class PhoneBook():
    def getContactByName(self,Name):
        return PC.Nambers.get(Name)
PC=PhoneContact()
PB=PhoneBook()
state=0
def get_state():
    return state
@bot.message_handler(commands=['add_namber'])
def add(message):
    bot.send_message(message.chat.id,"напишите сперва имя потом номер через пробел")
    global state
    state=1

@bot.message_handler(func=lambda message: get_state()==1)
def add1(message):
    try:
        message1=str(message.text).split()
        PC.appendContact(message1[0],message1[1])
    except:
        bot.send_message(message.chat.id,"ошибка")
    global state
    state=0
status=0
def get_status():
    return status
@bot.message_handler(commands=['get_namber'])
def get(message):
    bot.send_message(message.chat.id,"Напишите имя, номер которого хотите узнать.")
    global status
    status=1
@bot.message_handler(func=lambda message: get_status()==1)
def get1(message):
    bot.send_message(message.chat.id,str(PB.getContactByName(message.text)))
    global status
    status=0
bot.polling(none_stop=True, interval=1)