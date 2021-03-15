import telebot
import datetime
bot = telebot.TeleBot("1602598586:AAF2UGl6CBrUPA8km8BzqgswgwTQWjmjwqs")
keyboard_change = telebot.types.ReplyKeyboardMarkup(True)
keyboard_change.row("/Календарь", "/Расписание_звонков")
keyboard_weekdayOfTheWeek = telebot.types.ReplyKeyboardMarkup(True)
keyboard_weekdayOfTheWeek.row("/Сегодня", "/Завтра", "/На_всю_неделю", "/Вернуться")
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

@bot.message_handler(commands=['Расписание_звонков'])
def callShedule(callShedule):
  tid = callShedule.chat.id
  bot.send_message(tid, "1)8:00-9:35\n2)9:45-11:20\n3)11:45-13:20\n4)13:30-15:05\n5)15:30-17:05")

@bot.message_handler(commands=['Календарь'])
def calendar(calendar):
  tid = calendar.chat.id
  bot.send_message(tid, "Выберите какое расписание вам нужно", reply_markup = keyboard_weekdayOfTheWeek)


@bot.message_handler(commands=['Сегодня'])
def toweekday(toweekday):
  tid = toweekday.chat.id

  #Четная
  if (week == 0):
    bot.send_message(tid, "Четная неделя")

    if (weekday == 0):
      bot.send_message(tid, "Понедельник")
      bot.send_message(tid, "1) ИСиТ(Лаб) - 8:00-9:35(Бурмин Л.Н.)\nКабинет - 2139\n2) АВС(Лаб) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2139\n3) Прог(Лаб) - 11:45-13:20(Бурмин Л.Н.)\nКабинет - 2139")

    elif (weekday == 1):
      bot.send_message(tid, "Вторник")
      bot.send_message(tid, "1) Физ-ра - 8:00-9:35(Тюкалова С.А.)\nТир\n2) Высшая математика(Пр) - 9:45-11:20(Медведев А.В.)\nКабинет - 5121\n3) Высшая математика(Л) - 11:45-13:20(Медведев А.В.)\nКабинет - 5121\n4) ИСиТ(Л) - 13:30-15:05(Степанов Ю.А.)\nКабинет -2226")

    elif (weekday == 2):
      bot.send_message(tid, "Среда")
      bot.send_message(tid, "Выходной, пар нет")

    elif (weekday == 3):
      bot.send_message(tid, "Четверг")
      bot.send_message(tid, "1) АВС(Л) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2221\n2)Основы сис. анализа(Л) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 2221")

    elif (weekday == 4):
      bot.send_message(tid, "Пятница")
      bot.send_message(tid, "1) Англ(Лаб) - 9:45-11:20(Гринвальд О.Н.)\nКабинет - 2226\n2) История(Пр) - 11:45-13:20(Карпин А.В.)\nКабинет - 2226\n3) Экономика(Л) - 13:30-15:05(Саблин К.С.)\nКабинет - 2226\n4) Экономика(Пр) - 15:30-17:05(Попова Е.Ю.)\nКабинет - 2226")

    else:
      bot.send_message(tid, "Выходной")

  #Нечетная
  elif (week == 1):
    bot.send_message(tid, "Нечетная неделя")

    if (weekday == 0):
      bot.send_message(tid, "Понедельник")
      bot.send_message(tid, "1) ИСиТ(Лаб) - 8:00-9:35(Бурмин Л.Н.)\nКабинет - 2139\n2) АВС(Лаб) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2139\n3) Прог(Лаб) - 11:45-13:20(Бурмин Л.Н.)\nКабинет - 2139\n4) Физ-ра - 13:30-15:05(Тюкалова С.А.)")

    elif (weekday == 1):
      bot.send_message(tid, "Вторник")
      bot.send_message(tid, "1) Физ-ра - 8:00-9:35(Тюкалова С.А.)\nТир\n2) Высшая математика(Пр) - 9:45-11:20(Медведев А.В.)\nКабинет - 5121\n3) Высшая математика(Л) - 11:45-13:20(Медведев А.В.)\nКабинет - 5121\n4) Прог(Л) - 13:30-15:05(Бурмин Л.Н.)\nКабинет - 2226")
      
    elif (weekday == 2):
      bot.send_message(tid, "Среда")
      bot.send_message(tid, "1) БЖД(Л) - 15:30-17:05(Ефимов Д.А.)\n2 блочная")
      
    elif (weekday == 3):
      bot.send_message(tid, "Четверг")
      bot.send_message(tid, "1) БЖД(Пр) - 11:45-13:20(Немолочная Н.В.)\nКабинет - 2221\n2) Основы сис. анализа(Л) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 2221")
      
    elif (weekday == 4):
      bot.send_message(tid, "Пятница")
      bot.send_message(tid, "1) Англ(Лаб) - 9:45-11:20(Гринвальд О.Н.)\nКабинет - 2226\n2) История(Пр) - 11:45-13:20(Карпин А.В.)\nКабинет - 2226\n3) Экономика(Л) - 13:30-15:05(Саблин К.С.)\nКабинет - 2226\n4) Экономика(Пр) - 15:30-17:05(Попова Е.Ю.)\nКабинет - 2226")

    else:
      bot.send_message(tid, "Выходной")

    
      
@bot.message_handler(commands=['Завтра'])
def tomorrow(tomorrow):
  tid = tomorrow.chat.id

  #Четная
  if (week == 0):

    if (weekday == 0):
      bot.send_message(tid, "Четная неделя")
      bot.send_message(tid, "Вторник")
      bot.send_message(tid, "1) Физ-ра - 8:00-9:35(Тюкалова С.А.)\nТир\n2) Высшая математика(Пр) - 9:45-11:20(Медведев А.В.)\nКабинет - 5121\n3) Высшая математика(Л) - 11:45-13:20(Медведев А.В.)\nКабинет - 5121\n4) ИСиТ(Л) - 13:30-15:05(Степанов Ю.А.)\nКабинет -2226")

    elif (weekday == 1):
      bot.send_message(tid, "Четная неделя")
      bot.send_message(tid, "Среда")
      bot.send_message(tid, "Выходной, пар нет")

    elif (weekday == 2):
      bot.send_message(tid, "Четная неделя")
      bot.send_message(tid, "Четверг")
      bot.send_message(tid, "1) АВС(Л) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2221\n2)Основы сис. анализа(Л) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 2221")

    elif (weekday == 3):
      bot.send_message(tid, "Четная неделя")
      bot.send_message(tid, "Пятница")
      bot.send_message(tid, "1) Англ(Лаб) - 9:45-11:20(Гринвальд О.Н.)\nКабинет - 2226\n2) История(Пр) - 11:45-13:20(Карпин А.В.)\nКабинет - 2226\n3) История(Л) - 13:30-15:05(Карпин А.В.)\nКабинет - 2226")

    elif (weekday == 6):
      bot.send_message(tid, "Нечетная неделя")
      bot.send_message(tid, "Понедельник")
      bot.send_message(tid, "1) ИСиТ(Лаб) - 8:00-9:35(Бурмин Л.Н.)\nКабинет - 2139\n2) АВС(Лаб) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2139\n3) Прог(Лаб) - 11:45-13:20(Бурмин Л.Н.)\nКабинет - 2139\n4) Физ-ра - 13:30-15:05(Тюкалова С.А.)")
    
    else:
      bot.send_message(tid, "Выходной")

  #Нечетная
  elif (week == 1):

    if (weekday == 0):
      bot.send_message(tid, "Нечетная неделя")
      bot.send_message(tid, "Вторник")
      bot.send_message(tid, "1) Физ-ра - 8:00-9:35(Тюкалова С.А.)\nТир\n2) Высшая математика(Пр) - 9:45-11:20(Медведев А.В.)\nКабинет - 5121\n3) Высшая математика(Л) - 11:45-13:20(Медведев А.В.)\nКабинет - 5121\n4) Прог(Л) - 13:30-15:05(Бурмин Л.Н.)\nКабинет - 2226")
      
    elif (weekday == 1):
      bot.send_message(tid, "Нечетная неделя")
      bot.send_message(tid, "Среда")
      bot.send_message(tid, "1) БЖД(Л) - 15:30-17:05(Ефимов Д.А.)\n2 блочная")
      
    elif (weekday == 2):
      bot.send_message(tid, "Нечетная неделя")
      bot.send_message(tid, "Четверг")
      bot.send_message(tid, "1) БЖД(Пр) - 11:45-13:20(Немолочная Н.В.)\nКабинет - 2221\n2) Основы сис. анализа(Л) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 2221")
      
    elif (weekday == 3):
      bot.send_message(tid, "Нечетная неделя")
      bot.send_message(tid, "Пятница")
      bot.send_message(tid, "1) Англ(Лаб) - 9:45-11:20(Гринвальд О.Н.)\nКабинет - 2226\n2) История(Пр) - 11:45-13:20(Карпин А.В.)\nКабинет - 2226\n3) Экономика(Л) - 13:30-15:05(Саблин К.С.)\nКабинет - 2226\n4) Экономика(Пр) - 15:30-17:05(Попова Е.Ю.)\nКабинет - 2226")
    
    elif (weekday == 6):
      bot.send_message(tid, "Четная неделя")
      bot.send_message(tid, "Понедельник")
      bot.send_message(tid, "1) ИСиТ(Лаб) - 8:00-9:35(Бурмин Л.Н.)\nКабинет - 2139\n2) АВС(Лаб) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2139\n3) Прог(Лаб) - 11:45-13:20(Бурмин Л.Н.)\nКабинет - 2139")

    else:
      bot.send_message(tid, "Выходной")



@bot.message_handler(commands=['На_всю_неделю'])
def allWeek(allWeek):
  tid = allWeek.chat.id

  #Четная
  if (week == 0):
    bot.send_message(tid, "Четная неделя")
    bot.send_message(tid, "Понедельник")
    bot.send_message(tid, "1) ИСиТ(Лаб) - 8:00-9:35(Бурмин Л.Н.)\nКабинет - 2139\n2) АВС(Лаб) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2139\n3) Прог(Лаб) - 11:45-13:20(Бурмин Л.Н.)\nКабинет - 2139")
    
    bot.send_message(tid, "Вторник")
    bot.send_message(tid, "1) Физ-ра - 8:00-9:35(Тюкалова С.А.)\nТир\n2) Высшая математика(Пр) - 9:45-11:20(Медведев А.В.)\nКабинет - 5121\n3) Высшая математика(Л) - 11:45-13:20(Медведев А.В.)\nКабинет - 5121\n4) ИСиТ(Л) - 13:30-15:05(Степанов Ю.А.)\nКабинет -2226")

    bot.send_message(tid, "Среда")
    bot.send_message(tid, "Выходной, пар нет")

    bot.send_message(tid, "Четверг")
    bot.send_message(tid, "1) АВС(Л) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2221\n2)Основы сис. анализа(Л) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 2221")
    
    bot.send_message(tid, "Пятница")
    bot.send_message(tid, "1) Англ(Лаб) - 9:45-11:20(Гринвальд О.Н.)\nКабинет - 2226\n2) История(Пр) - 11:45-13:20(Карпин А.В.)\nКабинет - 2226\n3) История(Л) - 13:30-15:05(Карпин А.В.)\nКабинет - 2226")

  #Нечетная
  elif (week == 1):
    bot.send_message(tid, "Нечетная неделя")
    bot.send_message(tid, "Понедельник")
    bot.send_message(tid, "1) ИСиТ(Лаб) - 8:00-9:35(Бурмин Л.Н.)\nКабинет - 2139\n2) АВС(Лаб) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2139\n3) Прог(Лаб) - 11:45-13:20(Бурмин Л.Н.)\nКабинет - 2139\n4) Физ-ра - 13:30-15:05(Тюкалова С.А.)\nТир")
    
    bot.send_message(tid, "Вторник")
    bot.send_message(tid, "1) Физ-ра - 8:00-9:35(Тюкалова С.А.)\nТир\n2) Высшая математика(Пр) - 9:45-11:20(Медведев А.В.)\nКабинет - 5121\n3) Высшая математика(Л) - 11:45-13:20(Медведев А.В.)\nКабинет - 5121\n4) Прог(Л) - 13:30-15:05(Бурмин Л.Н.)\nКабинет - 2226")
   
    bot.send_message(tid, "Среда")
    bot.send_message(tid, "1) БЖД(Л) - 15:30-17:05(Ефимов Д.А.)\n2 блочная")

    bot.send_message(tid, "Четверг")
    bot.send_message(tid, "1) БЖД(Пр) - 11:45-13:20(Немолочная Н.В.)\nКабинет - 2221\n2) Основы сис. анализа(Л) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 2221")
   
    bot.send_message(tid, "Пятница")
    bot.send_message(tid, "1) Англ(Лаб) - 9:45-11:20(Гринвальд О.Н.)\nКабинет - 2226\n2) История(Пр) - 11:45-13:20(Карпин А.В.)\nКабинет - 2226\n3) Экономика(Л) - 13:30-15:05(Саблин К.С.)\nКабинет - 2226\n4) Экономика(Пр) - 15:30-17:05(Попова Е.Ю.)\nКабинет - 2226")



#Понедельник
@bot.message_handler(commands=['Пн', 'ПН', 'пн', 'пН', 'Понедельник' ,'понедельник' ,'пОНЕДЕЛЬНИК' ,'ПОНЕДЕЛЬНИК'])
def monweekday(monweekday):
  tid = monweekday.chat.id

  if (week == 0):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) ИСиТ(Лаб) - 8:00-9:35(Бурмин Л.Н.)\nКабинет - 2139\n2) АВС(Лаб) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2139\n3) Прог(Лаб) - 11:45-13:20(Бурмин Л.Н.)\nКабинет - 2139")

  if (week == 1):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) ИСиТ(Лаб) - 8:00-9:35(Бурмин Л.Н.)\nКабинет - 2139\n2) АВС(Лаб) - 9:45-11:20(Завозкин С.Ю.)\nКабинет - 2139\n3) Прог(Лаб) - 11:45-13:20(Бурмин Л.Н.)\nКабинет - 2139\n4) Физ-ра - 13:30-15:05(Тюкалова С.А.)\nТир")



#Вторник
@bot.message_handler(commands=['Вт' ,'ВТ' ,'вт' ,'вТ' ,'Вторник' ,'вторник' ,'вТОРНИК' ,'ВТОРНИК'])
def tuesweekday(tuesweekday):
  tid = tuesweekday.chat.id

  if (week == 0):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) Физ-ра - 8:00-9:35(Тюкалова С.А.)\nТир\n2) Высшая математика(Пр) - 9:45-11:20(Медведев А.В.)\nКабинет - 5121\n3) Высшая математика(Л) - 11:45-13:20(Медведев А.В.)\nКабинет - 5121\n4) ИСиТ(Л) - 13:30-15:05(Степанов Ю.А.)\nКабинет - 2226")

  if (week == 1):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) Физ-ра - 8:00-9:35(Тюкалова С.А.)\nТир\n2) Высшая математика(Пр) - 9:45-11:20(Медведев А.В.)\nКабинет - 5121\n3) Высшая математика(Л) - 11:45-13:20(Медведев А.В.)\nКабинет - 5121\n4) Прог(Л) - 13:30-15:05(Бурмин Л.Н.)\nКабинет -2226")


  
#Среда
@bot.message_handler(commands=['Ср' ,'СР' ,'ср' ,'сР' ,'Среда' ,'среда' ,'сРЕДА' ,'СРЕДА'])
def wednesweekday(wednesweekday):
  tid = wednesweekday.chat.id

  if (week == 0):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "Выходной, пар нет")

  if (week == 1):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) БЖД(Л) - 15:30-17:05(Ефимов Д.А.)\n2 блочная")



#Четверг
@bot.message_handler(commands=['Чт' ,'ЧТ' ,'чт' ,'чТ' ,'Четверг' ,'четверг' ,'чЕТВЕРГ' ,'ЧЕТВЕРГ'])
def thursweekday(thursweekday):
  tid = thursweekday.chat.id

  if (week == 0):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) АВС(Л) - 11:45-13:20(Завозкин С.Ю.)\nКабинет - 2221\n2)Основы сис. анализа(Л) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 2221")

  if (week == 1):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) БЖД(Пр) - 11:45-13:20(Немолочная Н.В.)\nКабинет - 2221\n2) Основы сис. анализа(Л) - 13:30-15:05(Мешечкин В.В.)\nКабинет - 2221")



#Пятница
@bot.message_handler(commands=['Пт' ,'ПТ' ,'пт' ,'пТ' ,'Пятница' ,'пятница' ,'пЯТНИЦА' ,'ПЯТНИЦА'])
def friweekday(friweekday):
  tid = friweekday.chat.id
  
  if (week == 0):
    bot.send_message(tid,"Четная неделя")
    bot.send_message(tid, "1) Англ(Лаб) - 9:45-11:20(Гринвальд О.Н.)\nКабинет - 2226\n2) История(Пр) - 11:45-13:20(Карпин А.В.)\nКабинет -  2226\n3) История(Л) - 13:30-15:05(Карпин А.В.)\nКабинет - 2226")

  if (week == 1):
    bot.send_message(tid,"Нечетная неделя")
    bot.send_message(tid, "1) Англ(Лаб) - 9:45-11:20(Гринвальд О.Н.)\nКабинет - 2226\n2) История(Пр) - 11:45-13:20(Карпин А.В.)\nКабинет - 2226\n3) Экономика(Л) - 13:30-15:05(Саблин К.С.)\nКабинет - 2226\n4) Экономика(Пр) - 15:30-17:05(Попова Е.Ю.)\nКабинет - 2226")


@bot.message_handler(content_types=['text'])
def sendYourMessage(message):
  mid = message.chat.id

  if message.text == "Привет":
    bot.send_message(mid, "Привет:)")
    
  elif message.text =="Пока":
    bot.send_message(mid, "Пока:(")

  else:
    bot.send_message(mid, "Сенпай, я хочу услышать другой вопрос")

bot.polling()
