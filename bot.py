import telebot
import datetime
bot = telebot.TeleBot("1602598586:AAF2UGl6CBrUPA8km8BzqgswgwTQWjmjwqs")
keyboard_change = telebot.types.ReplyKeyboardMarkup(True)
button_kalendar = telebot.types.KeyboardButton(text='Календарь')
keyboard_change.add(button_kalendar)
button_calls = telebot.types.KeyboardButton(text='Расписание звонков')
keyboard_change.add(button_calls)
keyboard_weekdayOfTheWeek = telebot.types.ReplyKeyboardMarkup(True)
button_today = telebot.types.KeyboardButton(text='Сегодня')
keyboard_weekdayOfTheWeek.add(button_today)
button_tommorow = telebot.types.KeyboardButton(text='Завтра')
keyboard_weekdayOfTheWeek.add(button_tommorow)
button_allWeek = telebot.types.KeyboardButton(text='На всю неделю')
keyboard_weekdayOfTheWeek.add(button_allWeek)
keyboard_weekdayOfTheWeek.row("/Вернуться")
week = (datetime.datetime.utcnow().isocalendar()[1])%2
weekday = datetime.datetime.today().weekday()


@bot.message_handler(commands=['help', 'Help'])
def help(help):
  tid = help.chat.id
  bot.send_message(tid,"Бот-календарь\nВыполнил работу Абраменко Константин\nСтудент КемГУ\nГруппа ПИ-203.")
  bot.send_message(tid, "Введите '/Пн' (Любой другой день недели), чтобы вывести расписание на этот день.")
  bot.send_message(tid, "Введите '/Сегодня' , чтобы вывести расписание на сегодняшний день.")
  bot.send_message(tid, "Введите '/Завтра' , чтобы вывести расписание на завтрашний день.")
  bot.send_message(tid, "Введите '/На_всю_неделю' , чтобы вывести расписание на всю неделю.")
  
@bot.message_handler(commands=['start', 'Start'])
def startWork(startWork):
  tid = startWork.chat.id
  bot.send_message(tid, "Введите /help чтобы посмотреть команды и информацию о боте")
  bot.send_message(tid, "start work!", reply_markup = keyboard_change) 

@bot.message_handler(commands=['Вернуться'])
def returnWork(returnWork):
  tid = returnWork.chat.id
  bot.send_message(tid, "start work!", reply_markup = keyboard_change)

#Понедельник
@bot.message_handler(commands=['Пн', 'ПН', 'пн'])
def monweekday(monweekday):
  tid = monweekday.chat.id

  if (week == 0):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) Прик. стат.(л) - 8:00-9:35(Инденко О.Н.)\nКабинет - 2бл\n2) Прик. стат.(пр) - 9:45-11:20(Инденко О.Н.)\nКабинет - 2141\n3) Опер. системы(л) - 11:45-13:20(Чеботарев)\nКабинет - 2226")

  if (week == 1):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) Прик. стат.(л) - 8:00-9:35(Инденко О.Н.)\nКабинет - 2бл\n2) Опер. системы(пр) - 9:45-11:20(Карабцев С.Н.)\nКабинет - 2130а\n3) Прик. стат.(пр) - 11:45-13:20(Инденко О.Н.)\nКабинет - 2141\n")



#Вторник
@bot.message_handler(commands=['Вт' ,'ВТ' ,'вт'])
def tuesweekday(tuesweekday):
  tid = tuesweekday.chat.id

  if (week == 0):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) Прог. инженер.(лаб) - 9:45-11:20(Илькевич В.В.)\nКабинет - 2130а\n2) БД(лаб) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2131в\n3) БД(л) - 13:30-15:05(Завозкин С.Ю.)\nКабинет - 2226\n4) Физра - 15:30-17:05(Мартыненко)\nПантера")

  if (week == 1):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) Прог. инженер.(лаб) - 9:45-11:20(Илькевич В.В.)\nКабинет - 2130а\n2) БД(лаб) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2131в\n3) Прог. инженер.(л) - 13:30-15:05(Гудов А.М.)\nКабинет - 2226\n4) Физра - 15:30-17:05(Мартыненко)\nПантера")


  
#Среда
@bot.message_handler(commands=['Ср' ,'СР' ,'ср'])
def wednesweekday(wednesweekday):
  tid = wednesweekday.chat.id

  if (week == 0):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) Фин. мат.(лаб) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 1517\n2) Комп. физика(л) - 15:30-17:05(Кравченко Н.Г.)\nКабинет - 5бл")

  if (week == 1):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) Комп. физика(лаб) - 11:45-13:20(Кравченко Н.Г.)\nКабинет - 1314\n2) Фин. мат.(лаб) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 1517")



#Четверг
@bot.message_handler(commands=['Чт' ,'ЧТ' ,'чт'])
def thursweekday(thursweekday):
  tid = thursweekday.chat.id

  if (week == 0):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) РМП(Пр) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2130а\n2) АПРиИИС(Л) - 13:30-15:05(Бурмин Л.Н.)\nКабинет - 2226")

  if (week == 1):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) РМП(Пр) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2130а\n2) РМП(Л) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2226")



#Пятница
@bot.message_handler(commands=['Пт' ,'ПТ' ,'пт'])
def friweekday(friweekday):
  tid = friweekday.chat.id
  
  if (week == 0):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) Комп. физика(лаб) - 13:30-15:05(Кравченко Н.Г.)\nКабинет - 1314\n2) Англ(Лаб) - 15:30-17:05(Гринвальд О.Н.)\nКабинет - 2229\n3) АПРиИИС(Л) - 17:15-18:50(Степанов И.Ю.)\nКабинет - 2130а")

  if (week == 1):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) Физра - 11:45-13:20(Мартыненко)\nПантера\n2) Фин. мат.(л) - 13:30-15:05(Крутиков В.Н.)\nКабинет - 2226\n3) Англ(Лаб) - 15:30-17:05(Гринвальд О.Н.)\nКабинет - 2229\n4) АПРиИИС(Л) - 17:15-18:50(Степанов И.Ю.)\nКабинет - 2130а")



#Понедельник следующий
@bot.message_handler(commands=['ПнСлед', 'ПНСлед', 'пнСлед'])
def nextmonweekday(nextmonweekday):
  tid = nextmonweekday.chat.id

  if (week == 1):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) Прик. стат.(л) - 8:00-9:35(Инденко О.Н.)\nКабинет - 2бл\n2) Прик. стат.(пр) - 9:45-11:20(Инденко О.Н.)\nКабинет - 2141\n3) Опер. системы(л) - 11:45-13:20(Чеботарев)\nКабинет - 2226")

  if (week == 0):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) Прик. стат.(л) - 8:00-9:35(Инденко О.Н.)\nКабинет - 2бл\n2) Опер. системы(пр) - 9:45-11:20(Карабцев С.Н.)\nКабинет - 2130а\n3) Прик. стат.(пр) - 11:45-13:20(Инденко О.Н.)\nКабинет - 2141\n") 



#Вторник следующий
@bot.message_handler(commands=['ВтСлед' ,'ВТСлед' ,'втСлед'])
def nexttuesweekday(nexttuesweekday):
  tid = nexttuesweekday.chat.id

  if (week == 1):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) Прог. инженер.(лаб) - 9:45-11:20(Илькевич В.В.)\nКабинет - 2130а\n2) БД(лаб) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2131в\n3) БД(л) - 13:30-15:05(Завозкин С.Ю.)\nКабинет - 2226\n4) Физра - 15:30-17:05(Мартыненко)\nПантера")

  if (week == 0):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) Прог. инженер.(лаб) - 9:45-11:20(Илькевич В.В.)\nКабинет - 2130а\n2) БД(лаб) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2131в\n3) Прог. инженер.(л) - 13:30-15:05(Гудов А.М.)\nКабинет - 2226\n4) Физра - 15:30-17:05(Мартыненко)\nПантера")


  
#Среда следующая
@bot.message_handler(commands=['СрСлед' ,'СРСлед' ,'срСлед'])
def nextwednesweekday(nextwednesweekday):
  tid = nextwednesweekday.chat.id

  if (week == 1):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) Фин. мат.(лаб) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 1517\n2) Комп. физика(л) - 15:30-17:05(Кравченко Н.Г.)\nКабинет - 5бл")

  if (week == 0):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) Комп. физика(лаб) - 11:45-13:20(Кравченко Н.Г.)\nКабинет - 1314\n2) Фин. мат.(лаб) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 1517")



#Четверг следующий
@bot.message_handler(commands=['ЧтСлед' ,'ЧТСлед' ,'чтСлед'])
def nextthursweekday(nextthursweekday):
  tid = nextthursweekday.chat.id

  if (week == 1):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) РМП(Пр) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2130а\n2) АПРиИИС(Л) - 13:30-15:05(Бурмин Л.Н.)\nКабинет - 2226")

  if (week == 0):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) РМП(Пр) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2130а\n2) РМП(Л) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2226")



#Пятница следующая
@bot.message_handler(commands=['ПтСлед' ,'ПТСлед' ,'птСлед'])
def nextfriweekday(nextfriweekday):
  tid = nextfriweekday.chat.id
  
  if (week == 0):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) Комп. физика(лаб) - 13:30-15:05(Кравченко Н.Г.)\nКабинет - 1314\n2) Англ(Лаб) - 15:30-17:05(Гринвальд О.Н.)\nКабинет - 2229\n3) АПРиИИС(Л) - 17:15-18:50(Степанов И.Ю.)\nКабинет - 2130а")

  if (week == 1):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) Физра - 11:45-13:20(Мартыненко)\nПантера\n2) Фин. мат.(л) - 13:30-15:05(Крутиков В.Н.)\nКабинет - 2226\n3) Англ(Лаб) - 15:30-17:05(Гринвальд О.Н.)\nКабинет - 2229\n4) АПРиИИС(Л) - 17:15-18:50(Степанов И.Ю.)\nКабинет - 2130а")


@bot.message_handler(content_types=['text'])
def textMessage(textMessage):
  if textMessage.text == "Расписание звонков":
    tid = textMessage.chat.id
    bot.send_message(tid, "1)8:00-9:35\n2)9:45-11:20\n3)11:45-13:20\n4)13:30-15:05\n5)15:30-17:05")

  if textMessage.text == "Календарь":
    tid = textMessage.chat.id
    bot.send_message(tid, "Выберите какое расписание вам нужно", reply_markup = keyboard_weekdayOfTheWeek)

  if textMessage.text == "Сегодня":
    tid = textMessage.chat.id
    #Четная
    if (week == 0):
      bot.send_message(tid, "Четная неделя")
      
      if (weekday == 0):
        bot.send_message(tid, "Понедельник")
        bot.send_message(tid, "1) Прик. стат.(л) - 8:00-9:35(Инденко О.Н.)\nКабинет - 2бл\n2) Прик. стат.(пр) - 9:45-11:20(Инденко О.Н.)\nКабинет - 2141\n3) Опер. системы(л) - 11:45-13:20(Чеботарев)\nКабинет - 2226")

      elif (weekday == 1):
        bot.send_message(tid, "Вторник")
        bot.send_message(tid, "1) Прог. инженер.(лаб) - 9:45-11:20(Илькевич В.В.)\nКабинет - 2130а\n2) БД(лаб) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2131в\n3) БД(л) - 13:30-15:05(Завозкин С.Ю.)\nКабинет - 2226\n4) Физра - 15:30-17:05(Мартыненко)\nПантера")

      elif (weekday == 2):
        bot.send_message(tid, "Среда")
        bot.send_message(tid, "1) Фин. мат.(лаб) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 1517\n2) Комп. физика(л) - 15:30-17:05(Кравченко Н.Г.)\nКабинет - 5бл")

      elif (weekday == 3):
        bot.send_message(tid, "Четверг")
        bot.send_message(tid, "1) РМП(Пр) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2130а\n2) АПРиИИС(Л) - 13:30-15:05(Бурмин Л.Н.)\nКабинет - 2226")

      elif (weekday == 4):
        bot.send_message(tid, "Пятница")
        bot.send_message(tid, "1) Комп. физика(лаб) - 13:30-15:05(Кравченко Н.Г.)\nКабинет - 1314\n2) Англ(Лаб) - 15:30-17:05(Гринвальд О.Н.)\nКабинет - 2229\n3) АПРиИИС(Л) - 17:15-18:50(Степанов И.Ю.)\nКабинет - 2130а")

      else:
        bot.send_message(tid, "Выходной")

    #Нечетная
    elif (week == 1):
      bot.send_message(tid, "Нечетная неделя")

      if (weekday == 0):
        bot.send_message(tid, "Понедельник")
        bot.send_message(tid, "1) Прик. стат.(л) - 8:00-9:35(Инденко О.Н.)\nКабинет - 2бл\n2) Опер. системы(пр) - 9:45-11:20(Карабцев С.Н.)\nКабинет - 2130а\n3) Прик. стат.(пр) - 11:45-13:20(Инденко О.Н.)\nКабинет - 2141\n")

      elif (weekday == 1):
        bot.send_message(tid, "Вторник")
        bot.send_message(tid, "1) Прог. инженер.(лаб) - 9:45-11:20(Илькевич В.В.)\nКабинет - 2130а\n2) БД(лаб) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2131в\n3) Прог. инженер.(л) - 13:30-15:05(Гудов А.М.)\nКабинет - 2226\n4) Физра - 15:30-17:05(Мартыненко)\nПантера")
        
      elif (weekday == 2):
        bot.send_message(tid, "Среда")
        bot.send_message(tid, "1) Комп. физика(лаб) - 11:45-13:20(Кравченко Н.Г.)\nКабинет - 1314\n2) Фин. мат.(лаб) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 1517")
        
      elif (weekday == 3):
        bot.send_message(tid, "Четверг")
        bot.send_message(tid, "1) РМП(Пр) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2130а\n2) РМП(Л) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2226")
        
      elif (weekday == 4):
        bot.send_message(tid, "Пятница")
        bot.send_message(tid, "1) Физра - 11:45-13:20(Мартыненко)\nПантера\n2) Фин. мат.(л) - 13:30-15:05(Крутиков В.Н.)\nКабинет - 2226\n3) Англ(Лаб) - 15:30-17:05(Гринвальд О.Н.)\nКабинет - 2229\n4) АПРиИИС(Л) - 17:15-18:50(Степанов И.Ю.)\nКабинет - 2130а")

      else:
        bot.send_message(tid, "Выходной")

    
      
  if textMessage.text == "Завтра":
    tid = textMessage.chat.id
    #Четная
    if (week == 0):

      if (weekday == 0):
        bot.send_message(tid, "Четная неделя")
        bot.send_message(tid, "Вторник")
        bot.send_message(tid, "1) Прог. инженер.(лаб) - 9:45-11:20(Илькевич В.В.)\nКабинет - 2130а\n2) БД(лаб) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2131в\n3) БД(л) - 13:30-15:05(Завозкин С.Ю.)\nКабинет - 2226\n4) Физра - 15:30-17:05(Мартыненко)\nПантера")


      elif (weekday == 1):
        bot.send_message(tid, "Четная неделя")
        bot.send_message(tid, "Среда")
        bot.send_message(tid, "1) Фин. мат.(лаб) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 1517\n2) Комп. физика(л) - 15:30-17:05(Кравченко Н.Г.)\nКабинет - 5бл")

      elif (weekday == 2):
        bot.send_message(tid, "Четная неделя")
        bot.send_message(tid, "Четверг")
        bot.send_message(tid, "1) РМП(Пр) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2130а\n2) АПРиИИС(Л) - 13:30-15:05(Бурмин Л.Н.)\nКабинет - 2226")

      elif (weekday == 3):
        bot.send_message(tid, "Четная неделя")
        bot.send_message(tid, "Пятница")
        bot.send_message(tid, "1) Комп. физика(лаб) - 13:30-15:05(Кравченко Н.Г.)\nКабинет - 1314\n2) Англ(Лаб) - 15:30-17:05(Гринвальд О.Н.)\nКабинет - 2229\n3) АПРиИИС(Л) - 17:15-18:50(Степанов И.Ю.)\nКабинет - 2130а")

      elif (weekday == 6):
        bot.send_message(tid, "Нечетная неделя")
        bot.send_message(tid, "Понедельник")
        bot.send_message(tid, "1) Прик. стат.(л) - 8:00-9:35(Инденко О.Н.)\nКабинет - 2бл\n2) Опер. системы(пр) - 9:45-11:20(Карабцев С.Н.)\nКабинет - 2130а\n3) Прик. стат.(пр) - 11:45-13:20(Инденко О.Н.)\nКабинет - 2141\n")
      
      else:
        bot.send_message(tid, "Выходной")

    #Нечетная
    elif (week == 1):

      if (weekday == 0):
        bot.send_message(tid, "Нечетная неделя")
        bot.send_message(tid, "Вторник")
        bot.send_message(tid, "1) Прог. инженер.(лаб) - 9:45-11:20(Илькевич В.В.)\nКабинет - 2130а\n2) БД(лаб) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2131в\n3) Прог. инженер.(л) - 13:30-15:05(Гудов А.М.)\nКабинет - 2226\n4) Физра - 15:30-17:05(Мартыненко)\nПантера")
        
      elif (weekday == 1):
        bot.send_message(tid, "Среда")
        bot.send_message(tid, "1) Комп. физика(лаб) - 11:45-13:20(Кравченко Н.Г.)\nКабинет - 1314\n2) Фин. мат.(лаб) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 1517")
        
      elif (weekday == 2):
        bot.send_message(tid, "Нечетная неделя")
        bot.send_message(tid, "Четверг")
        bot.send_message(tid, "1) РМП(Пр) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2130а\n2) РМП(Л) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2226")
        
      elif (weekday == 3):
        bot.send_message(tid, "Нечетная неделя")
        bot.send_message(tid, "Пятница")
        bot.send_message(tid, "1) Физра - 11:45-13:20(Мартыненко)\nПантера\n2) Фин. мат.(л) - 13:30-15:05(Крутиков В.Н.)\nКабинет - 2226\n3) Англ(Лаб) - 15:30-17:05(Гринвальд О.Н.)\nКабинет - 2229\n4) АПРиИИС(Л) - 17:15-18:50(Степанов И.Ю.)\nКабинет - 2130а")
      
      elif (weekday == 6):
        bot.send_message(tid, "Четная неделя")
        bot.send_message(tid, "Понедельник")
        bot.send_message(tid, "1) Прик. стат.(л) - 8:00-9:35(Инденко О.Н.)\nКабинет - 2бл\n2) Прик. стат.(пр) - 9:45-11:20(Инденко О.Н.)\nКабинет - 2141\n3) Опер. системы(л) - 11:45-13:20(Чеботарев)\nКабинет - 2226")

      else:
        bot.send_message(tid, "Выходной")


  if textMessage.text == "На всю неделю":
    tid = textMessage.chat.id

    #Четная
    if (week == 0):
      bot.send_message(tid, "Четная неделя")
      bot.send_message(tid, "Понедельник")
      bot.send_message(tid, "1) Прик. стат.(л) - 8:00-9:35(Инденко О.Н.)\nКабинет - 2бл\n2) Прик. стат.(пр) - 9:45-11:20(Инденко О.Н.)\nКабинет - 2141\n3) Опер. системы(л) - 11:45-13:20(Чеботарев)\nКабинет - 2226")
      
      bot.send_message(tid, "Вторник")
      bot.send_message(tid, "1) Прог. инженер.(лаб) - 9:45-11:20(Илькевич В.В.)\nКабинет - 2130а\n2) БД(лаб) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2131в\n3) БД(л) - 13:30-15:05(Завозкин С.Ю.)\nКабинет - 2226\n4) Физра - 15:30-17:05(Мартыненко)\nПантера")

      bot.send_message(tid, "Среда")
      bot.send_message(tid, "1) Фин. мат.(лаб) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 1517\n2) Комп. физика(л) - 15:30-17:05(Кравченко Н.Г.)\nКабинет - 5бл")

      bot.send_message(tid, "Четверг")
      bot.send_message(tid, "1) РМП(Пр) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2130а\n2) АПРиИИС(Л) - 13:30-15:05(Бурмин Л.Н.)\nКабинет - 2226")
      
      bot.send_message(tid, "Пятница")
      bot.send_message(tid, "1) Комп. физика(лаб) - 13:30-15:05(Кравченко Н.Г.)\nКабинет - 1314\n2) Англ(Лаб) - 15:30-17:05(Гринвальд О.Н.)\nКабинет - 2229\n3) АПРиИИС(Л) - 17:15-18:50(Степанов И.Ю.)\nКабинет - 2130а")

    #Нечетная
    elif (week == 1):
      bot.send_message(tid, "Нечетная неделя")
      bot.send_message(tid, "Понедельник")
      bot.send_message(tid, "1) Прик. стат.(л) - 8:00-9:35(Инденко О.Н.)\nКабинет - 2бл\n2) Опер. системы(пр) - 9:45-11:20(Карабцев С.Н.)\nКабинет - 2130а\n3) Прик. стат.(пр) - 11:45-13:20(Инденко О.Н.)\nКабинет - 2141\n")
      
      bot.send_message(tid, "Вторник")
      bot.send_message(tid, "1) Прог. инженер.(лаб) - 9:45-11:20(Илькевич В.В.)\nКабинет - 2130а\n2) БД(лаб) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2131в\n3) Прог. инженер.(л) - 13:30-15:05(Гудов А.М.)\nКабинет - 2226\n4) Физра - 15:30-17:05(Мартыненко)\nПантера")
    
      bot.send_message(tid, "Среда")
      bot.send_message(tid, "1) Комп. физика(лаб) - 11:45-13:20(Кравченко Н.Г.)\nКабинет - 1314\n2) Фин. мат.(лаб) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 1517")

      bot.send_message(tid, "Четверг")
      bot.send_message(tid, "1) РМП(Пр) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2130а\n2) РМП(Л) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2226")
    
      bot.send_message(tid, "Пятница")
      bot.send_message(tid, "1) Физра - 11:45-13:20(Мартыненко)\nПантера\n2) Фин. мат.(л) - 13:30-15:05(Крутиков В.Н.)\nКабинет - 2226\n3) Англ(Лаб) - 15:30-17:05(Гринвальд О.Н.)\nКабинет - 2229\n4) АПРиИИС(Л) - 17:15-18:50(Степанов И.Ю.)\nКабинет - 2130а")

bot.polling()
