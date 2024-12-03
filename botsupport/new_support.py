from telebot import types
import telebot
import requests
import config
from dotenv import dotenv_values
from supporthelper.helper import *
from telebot.apihelper import answer_callback_query
import os
from data_base.data_base_users import Database
from telebot.types import ReplyKeyboardRemove

db = Database("C:/Users/Dreimond/PycharmProjects/FinalBotSupport/data_base/database.db")

SAVE_FOLDER = 'photos'

config_1 = dotenv_values("../.env")
TOKEN = config_1.get('TOKEN')
ADMIN_ID = config_1.get('ADMIN_ID')

user_emails = {}
user_state = {}
user_passwords= {}
user_new_emails = {}
user_new_pass={}
user_new_name={}
needHelp = []

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)
bot=telebot.TeleBot(TOKEN)


def typessupport(user_id):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    butOne=types.KeyboardButton("Account")
    butTwo=types.KeyboardButton("KYS")
    butThree=types.KeyboardButton("Deposit/Withdrawal of currencies")
    butFour=types.KeyboardButton("Buying/selling cryptocurrency (fiat/P2P)")
    butFive=types.KeyboardButton("Other")
    butSix=types.KeyboardButton("Write to support")
    markup.add(butOne,butTwo,butThree,butFive,butSix,butFour)
    bot.send_message(user_id,"Choose ",reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == '1':
        answer_callback=" The documents have expired"
        bot.answer_callback_query(call.id, "You choose The documents have expired✅")
        kys_reset_types(answer_callback)
    elif call.data == '2':
        answer_callback = " Update your country of residence"
        bot.answer_callback_query(call.id, "You choose Update your country of residence ✅")
        kys_reset_types(answer_callback)
    elif call.data == '3':
        answer_callback = " Name changed in documents"
        bot.answer_callback_query(call.id, "You choose Name changed in documents✅")
        kys_reset_types(answer_callback)
    elif call.data == '4':
        answer_callback = " Code changed in documents"
        bot.answer_callback_query(call.id, "You choose  Code changed in documents✅")
        kys_reset_types(answer_callback)
    elif call.data == '5':
        answer_callback = " Nationality changed"
        bot.answer_callback_query(call.id, "You choose  Nationality changed✅")
        kys_reset_types(answer_callback)
    elif call.data == '6':
        answer_callback = " Updating documents for using the fiat channel"
        bot.answer_callback_query(call.id, "You choose  Updating documents for using the fiat channel✅")
        kys_reset_types(answer_callback)
    elif call.data == '7':
        answer_callback = " Update documents according to Binance Card requirements"
        bot.answer_callback_query(call.id, "You choose  Update documents according to Binance Card requirements✅")
        kys_reset_types(answer_callback)
    bot.edit_message_text("You choose: " + answer_callback, chat_id=call.message.chat.id, message_id=call.message.message_id)


@bot.message_handler(commands=["WriteToSupport"])
def support(message):
    need_help_file = open("C:/Users/Dreimond/Desktop/testhelp.txt", "a", encoding='utf-8')


    if message.chat.id > 0:
        need_help_file.write(str(message.chat.id) + "\n" + str(message.chat.first_name) + "\n")
    else:
        need_help_file.write(str(message.chat.id) + "\n" + str(message.chat.title) + "\n")
    need_help_file.close()
    support_file = open("C:/Users/Dreimond/Desktop/testpython.txt", "r", encoding='utf-8')
    support_team = {str(586722554)}
    for line in support_file:
        support_team.add(line.strip())
    support_file.close()

    bot.send_message(
        message.chat.id,
        '''Wait a bit {0.first_name}, we sent your message to support! 
Please don't send any more messages. \nYou are in the queue.'''.format(message.from_user),
        parse_mode="html"
    )

    text_message = message.text[message.text.find(" ") + 1:] if message.text.find(" ") != -1 else "No message provided"

    for user in support_team:
        if user.isdigit():
            bot.send_message(int(user), f"{message.chat.id} ({message.chat.first_name}): {text_message}")
        else:
            print(f"Skipping invalid user ID: {user}")


@bot.message_handler(commands=["answer"])
def answer(message):
    support_file = open("C:/Users/Dreimond/Desktop/testpython.txt", "r", encoding='utf-8')
    support_team = {str(586722554)}
    for line in support_file:
        support_team.add(line.strip())
    support_file.close()

    if str(message.chat.id) in support_team:
        needHelp = []
        need_help_file = open("C:/Users/Dreimond/Desktop/testhelp.txt", "r", encoding='utf-8')
        for line in need_help_file:
            needHelp.append(line.strip())
        need_help_file.close()
        for user in support_team:
            if user.isdigit():
                if message.chat.id > 0:
                    bot.send_message(user,
                                     f"{message.chat.id} ({message.chat.first_name}): Answering to {needHelp[0]} {message.text[message.text.find(' ') + 1:]}")
                else:
                    bot.send_message(user,
                                     f"{message.chat.id} ({message.chat.title}): Answering to {needHelp[0]} {message.text[message.text.find(' ') + 1:]}")
        bot.send_message(int(needHelp[0]), f"Support: {message.text[message.text.find(' ') + 1:]}")
        with open("C:/Users/Dreimond/Desktop/testhelp.txt", "r", encoding='utf-8') as nhf:
            lines = nhf.readlines()
        with open("C:/Users/Dreimond/Desktop/testhelp.txt", "w", encoding='utf-8') as nhf:
            for line in lines:
                if line.strip("\n") != needHelp[0]:
                    nhf.write(line)
    else:
        bot.send_message(
            message.chat.id,
            f'You don\'t have permission to answer {message.text[message.text.find(" ") + 1:]}',
            parse_mode="html"
        )


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"This support Binance crypto bot")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    butOne=types.KeyboardButton("Autification")
    butTwo=types.KeyboardButton("/close")
    markup.add(butOne,butTwo)
    bot.send_message(message.chat.id,"Autification in crypto bot",reply_markup=markup)

@bot.message_handler(commands=["close"])
def close(message):
    bot.send_message(message.chat.id,"<em><b>Thank you.We stay with you</b></em>",parse_mode="html")
    bot.send_message(
        message.chat.id,
        "Goodbye!",
        reply_markup=ReplyKeyboardRemove()
    )
    chat_id = message.chat.id
    last_message_id = message.message_id
    for msg_id in range(last_message_id, last_message_id - 100, -1):
        try:
            bot.delete_message(chat_id, msg_id)
        except:
            pass

@bot.message_handler(content_types=['text','photo'])
def buttonsupport(message):
    user_id = message.chat.id
    if user_id not in user_state:
        user_state[user_id] = None
    if user_id not in user_emails:
        user_emails[user_id] = None

    if user_state[user_id] == "waiting_for_photo":
        try:
            photo = message.photo[-1]
            file_info = bot.get_file(photo.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            file_name = f"{SAVE_FOLDER}/{photo.file_id}.jpg"
            handle_photo(downloaded_file, file_name)
            bot.send_message(user_id, f"Your photo has been saved as {file_name}.✅")
            user_state[user_id] = None
        except Exception as e:
            bot.send_message(user_id, f"An error occurred: {e}")

    if user_state.get(user_id) == "waiting_for_new_appealing":
        user_appealing_text=message.text.strip()
        user_problem_appealing(user_appealing_text, user_id)
        bot.send_message(user_id, f"Your data {user_appealing_text}✅")
        user_id = message.from_user.id

    if user_state.get(user_id) == "waiting_for_data":
        user_date_reset = message.text.strip()
        data_about=str(user_date_reset)
        inheritance_data(data_about,user_id)
        bot.send_message(user_id, f"Your data {user_date_reset}✅")
        user_id = message.from_user.id
    if user_state.get(user_id)=="waiting_for_birth_reset":
       user_date_reset=message.text.strip()
       old_email = user_new_emails[user_id]
       new_date(user_date_reset, old_email)
       bot.send_message(user_id, f"Your new date {user_date_reset}✅")

    if user_state.get(user_id)=="waiting_for_new_address":
        user_new_address = message.text.strip()
        new_address(user_new_address)
        bot.send_message(user_id, f"Your address reset {user_new_address}✅")
    if user_state.get(user_id)=="waiting_for_name_reset":
       user_name_reset=message.text.strip()
       name_user=user_name_reset
       old_email = user_new_emails[user_id]
       new_name(name_user,old_email)
       bot.send_message(user_id, f"Your name reset {name_user}✅")
       print(user_name_reset)
    if user_state.get(user_id)=="waiting_for_password_reset":
        user_new_password=message.text.strip()
        old_pass=user_passwords[user_id]
        user_pass_data=db.get_user_by_password(old_pass)
        if not user_pass_data:
            bot.send_message(user_id, f"Your password not correct,write again❌")
        else:
            old_email = user_new_emails[user_id]
            pass_changes(user_new_password,old_email)
            bot.send_message(user_id, f"Your password was reset from {old_pass} on {user_new_password}✅")
            print(old_email)
    if user_state.get(user_id)=="waiting_for_new_email":
        user_new_email = message.text.strip()
        old_email =  user_new_emails[user_id]
        changes(user_new_email, old_email)
        bot.send_message(user_id, f"Your email was reset from {old_email} on {user_new_email}✅")
        user_state[user_id] = None
    if user_state.get(user_id) == "waiting_for_email":
        user_email = message.text.strip()
        bot.send_message(user_id, f" {user_email}")
        user_new_emails[user_id] = user_email
        user_data = db.get_user_by_email(user_email)
        email_for_all(user_email)
        if not user_data:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            butOne = types.KeyboardButton("<----")
            butTwo = types.KeyboardButton("/close")
            markup.add(butOne, butTwo)
            bot.send_message(message.chat.id, "Email was not registered.🔒Try again ", reply_markup=markup)
            user_state[user_id] = "waiting_for_email"
        else:
            bot.send_message(message.chat.id,"Email was registred✅ ")
            bot.send_message(message.chat.id, "Write your password 🖊️")
            user_state[user_id] = None
            user_state[user_id] = "waiting_for_password"
    elif user_state.get(user_id) == "waiting_for_password":
        user_password = message.text.strip()
        user_passwords[user_id]=user_password
        user_data_pass=db.get_user_by_password(user_password)
        if not user_data_pass:
            bot.send_message(user_id, f" Incorrect password write again❌🖊️ ")
            user_state[user_id] = "waiting_for_password"
        else:
            bot.send_message(user_id, f" Correct Password 🔓")
            typessupport(user_id)
            user_state[user_id] = None
    if message.text == "Autification":
        bot.send_message(user_id, "Please enter your email🖊️:")
        user_state[user_id] = "waiting_for_email"

    if message.text == "Account":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne = types.KeyboardButton("Reset 2FA")
        butTwo = types.KeyboardButton("Password reset")
        butThree = types.KeyboardButton("Account reactivation")
        butFour = types.KeyboardButton("Correction of name/date of birth")
        butFive = types.KeyboardButton("Inheritance of inheritance")
        butSix = types.KeyboardButton("Failed to unlock account")
        butSeven = types.KeyboardButton("<----")
        butEight = types.KeyboardButton("/close")
        butNine = types.KeyboardButton("Email reset")
        markup.add(butOne, butTwo, butThree, butFive, butSix, butFour, butSeven, butEight,butNine)
        bot.send_message(message.chat.id, "Choose ⌛️", reply_markup=markup)
    elif message.text == "KYS":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne = types.KeyboardButton("Appeal regarding facial verification rejected")
        butTwo = types.KeyboardButton("Change of residence your address")
        butThree = types.KeyboardButton("KYC reset")
        butFour = types.KeyboardButton("Appealing KYC rejection")
        butFive = types.KeyboardButton("<----")
        butSix = types.KeyboardButton("/close")
        markup.add(butOne, butTwo, butThree, butFive, butSix, butFour)
        bot.send_message(message.chat.id, "Choose ", reply_markup=markup)
    elif message.text == "Deposit/Withdrawal of currencies":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne = types.KeyboardButton("Cryptocurrency deposit not received")
        butTwo = types.KeyboardButton("Appeal regarding cancellation of cryptocurrency withdrawal")
        butThree = types.KeyboardButton("Appeal regarding suspension of cryptocurrency withdrawals")
        butFour = types.KeyboardButton("Transaction history")
        butFive = types.KeyboardButton("<----")
        butSix = types.KeyboardButton("/close")
        markup.add(butOne, butTwo, butThree, butFive, butSix, butFour)
        bot.send_message(message.chat.id, "Choose ⌛️", reply_markup=markup)
    elif message.text == "Buying/selling cryptocurrency (fiat/P2P)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne = types.KeyboardButton("Appeal regarding non-receipt of fiat deposit")
        butTwo = types.KeyboardButton("Fiat deposit suspension")
        butThree = types.KeyboardButton("Withdrawn fiat not received")
        butFour = types.KeyboardButton("Fraud/chargeback appeal")
        butFive = types.KeyboardButton("Appeal regarding P2P performance indicators")
        butSix = types.KeyboardButton("Assets frozen due to P2P dispute")
        butSeven = types.KeyboardButton("Unblocking P2P features")
        butEight = types.KeyboardButton("Receipts for P2P orders")
        butNine = types.KeyboardButton("<----")
        butTen = types.KeyboardButton("/close")
        markup.add(butOne, butTwo, butThree, butFive, butSix, butFour, butSeven, butEight, butNine, butTen)
        bot.send_message(message.chat.id, "Choose ⌛️", reply_markup=markup)
    elif message.text == "Other":
        bot.send_message(
            message.chat.id,
        '''(Ми завжди стурбовані тим, що користувач Binance міг стати жертвою шахрайства[введення його в оману з метою продажу активів чи виплати коштів]. Ми рекомендуємо вам негайно звернутись до місцевих правоохоронних органів.
        Якщо в результаті шахрайства ви вважаєте,що ваш акаунт Binance був скомпрометований,виконайте негайні заходи для його захисту і за необхідності зверніться за допомогою до нашої цілодобової служби підтримки клієнтів.
        Як захистити свій акаунт Binance від шахрайства
        Попередження про зростання кількості криптошахраїв
        Як вимкнути мій акаунт
        Якщо ви вважаєте, що вас ошукали, будь ласка, прочитайте важливі примітки, а потім натисніть нижче, щоб підтвердити свою згоду з ними та заповнити форму скарги, яка призначена для збору відповідної інформації в одному місці. Ознайомтеся з нашими примітками щодо заповнення форми.
        Важливі умови:
        1) Роль Binance не полягає в забезпеченні правопорядку, і ми не можемо гарантувати конкретного результату вашої скарги. Ми можемо переглядати ваші матеріали, однак робимо це на тій підставі, що не несемо жодної відповідальності перед вами за це чи щодо того, як або що ми будемо/не будемо робити у відповідь.
        2) Binance не несе відповідальності за зміст або будь-які дії, ужиті на платформах, що не належать Binance.
        3) Наша здатність діяти також регулюється місцевими законами та правилами, а також правами (і нашими обов’язками щодо) інших Користувачів Binance. Можливо, ми не зробимо або не зможемо зробити кроки, на які ви розраховуєте. З цієї причини, будь ласка, також негайно повідомите про цей інцидент місцевим правоохоронним органам.
        4) Ми намагатимемося інформувати вас про перебіг розслідування, але не гарантуємо цього. Іноді закон або інші юридичні обов’язки не дозволяють нам говорити про поточні розслідування.
        5) Надаючи нам свою інформацію, ви погоджуєтесь на обробку нами ваших персональних даних для проведення розслідування за цією скаргою. Будь-яка інформація, яку ви надсилаєте нам, також може бути передана правоохоронним органам. Ми оброблятимемо ваші дані відповідно до нашого повідомлення про конфіденційність. 
        Ваша скарга та наша відповідь на неї є конфіденційними.
        6) Надсилаючи скаргу на цьому порталі, ви погоджуєтесь в обмін на розгляд вашої скарги відмовитися від будь-яких претензій до операторів Binance щодо заявлених питань.
        Натиснувши кнопку нижче, ви погоджуєтесь з цими умовами та перейдете до форми звіту. Не натискайте кнопку, якщо не згодні.)''',

        )
    elif message.text == "<----":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne = types.KeyboardButton("Account")
        butTwo = types.KeyboardButton("KYS")
        butThree = types.KeyboardButton("Deposit/Withdrawal of currencies")
        butFour = types.KeyboardButton("Buying/selling cryptocurrency (fiat/P2P)")
        butFive = types.KeyboardButton("Other")
        butSix = types.KeyboardButton("Write to support")
        markup.add(butOne, butTwo, butThree, butFive, butSix, butFour)
        bot.send_message(message.chat.id, "Choose ⌛️", reply_markup=markup)
    elif message.text == "Reset 2FA":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne = types.KeyboardButton("email")
        butTwo = types.KeyboardButton("number")
        butThree = types.KeyboardButton("app autificator")
        butFour = types.KeyboardButton("key to enter")
        butFive = types.KeyboardButton("<----")
        markup.add(butOne, butTwo, butThree, butFour,butFive)
        bot.send_message(message.chat.id, "Choose to reset ⌛️", reply_markup=markup)
    elif message.text == "Email reset":
        bot.send_message(user_id, "Please enter your  new email🖊️:")
        user_state[user_id] = "waiting_for_new_email"
    if message.text == "email":
        check_data={"two_factor_ae":"False"}
        if db.check_multiple_conditions(check_data):
            bot.send_message(message.chat.id, "Email 2FA Connect  ✅")
            old_email = user_new_emails[user_id]
            fa_email(old_email)
            print("1")
        else:
            bot.send_message(message.chat.id, "Email 2FA delete ❌")
            old_email = user_new_emails[user_id]
            fa_email(old_email)
            print("2")
    if message.text == "number":
        check_data={"two_factor_an":"True"}
        if db.check_multiple_conditions(check_data):
            bot.send_message(message.chat.id, "number 2FA delete ❌")
            old_email = user_new_emails[user_id]
            fa_number(old_email)
        else:
            bot.send_message(message.chat.id, "Number 2FA Connect  ✅")
            old_email = user_new_emails[user_id]
            fa_number(old_email)
    if message.text == "app autificator":
        check_data={"two_factor_aa":"False"}
        if db.check_multiple_conditions(check_data):
            bot.send_message(message.chat.id, "App 2FA Connect  ✅")
            old_email = user_new_emails[user_id]
            fa_app(old_email)
        else:
            bot.send_message(message.chat.id, "App 2FA delete ❌")
            old_email = user_new_emails[user_id]
            fa_app(old_email)
    if message.text == "key to enter":
        check_data={"two_factor_ak":"False"}
        if db.check_multiple_conditions(check_data):
            bot.send_message(message.chat.id, "Key 2FA Connect ✅ ")
            old_email = user_new_emails[user_id]
            fa_key(old_email)
        else:
            bot.send_message(message.chat.id, "Key 2FA delete ❌")
            old_email = user_new_emails[user_id]
            fa_key(old_email)
    if message.text == "Password reset":
        bot.send_message(user_id, "Please enter your  new password🖊️:")
        user_state[user_id] = "waiting_for_password_reset"
    if message.text == "Correction of name/date of birth":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne = types.KeyboardButton("Correction of name")
        butTwo = types.KeyboardButton("Correction date of birth")
        butThree = types.KeyboardButton("<----")
        markup.add(butOne, butTwo,butThree)
        bot.send_message(message.chat.id, "Choose to correct ", reply_markup=markup)
    elif message.text == "Correction of name":
        bot.send_message(user_id, "Please enter your  new Name🖊️:")
        user_state[user_id] = "waiting_for_name_reset"
    elif message.text == "Correction date of birth":
        bot.send_message(user_id, "Please enter your  new birth format🖊️->(10.10.1900):")
        user_state[user_id] = "waiting_for_birth_reset"
    if message.text == "Account reactivation":
        bot.send_message(
            message.chat.id,
            '''(To be safe, please update your password and make sure your email address, phone verification or Google Authenticator are only available to you.
                The process may take up to 3 business days. Be kind, be patient while the information is being verified..)''',
        )
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne = types.KeyboardButton("Accept reactivation")
        butTwo = types.KeyboardButton("<----")
        markup.add(butOne, butTwo)
        bot.send_message(message.chat.id, "Choose to accept ⌛️", reply_markup=markup)
    elif message.text == "Accept reactivation":
        old_email = user_new_emails[user_id]
        reactivation(old_email)
        bot.send_message(user_id, " Reactivation was accept:✅")


    if message.text == "Inheritance of inheritance":
        bot.send_message(
            message.chat.id,
            '''(Appeal for inheritance,\n Appeal Requirements\n*Please note:\n
1. To file a claim, claimants must create a new account or log in to their existing account. Please do not submit a claim while logged in to the deceased’s account.
2. Please provide notarized or certified copies of the following documents with English translations (if the original documents are not in English):*)
Information about the deceased user's Binance account
Please provide the deceased user's Binance ID, email address, or phone number.
Additional materials
1. Certified copy of the last will/administrative letter/certificate of succession/court decision on the entry into force of the will or other legal documents confirming your right to ownership of the deceased's assets
2. Certified copy of the death certificate
3. Certified copy of the deceased's state-issued ID
4. Certified copy of your state-issued ID
Additional information
''',
        )
        user_state[user_id]="waiting_for_data"

    if message.text =="Failed to unlock account":
        check_data = {"Activating": "True"}
        if db.check_multiple_conditions(check_data):
            bot.send_message(message.chat.id, "Acc not need to activating ")
        else:
            bot.send_message(user_id, "Wait for activaiting:")
            old_email = user_new_emails[user_id]
            activating_acc(old_email)

    if message.text=="Appeal regarding facial verification rejected":
        bot.send_message(user_id, " Do yo want facial verification rejected?:")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne = types.KeyboardButton("Accept facial verification rejected")
        butTwo = types.KeyboardButton("<----")
        markup.add(butOne, butTwo)
        bot.send_message(message.chat.id, "Choose to accept ", reply_markup=markup)
    elif message.text == "Accept facial verification rejected":
        bot.send_message(user_id, " Send your photo to accept:")
        user_state[user_id] = "waiting_for_photo"

    if message.text=="KYC reset":
        bot.send_message(
            message.chat.id,
            '''(Declaration
    1. Please note that resetting your certification is a high-risk operation that may result in account loss, loss of assets, 
irreversible changes to your account status, and other risks.
    2. When you click the "Confirm Update" button, your account will be limited to withdrawals only until your new 
information is verified. All other functions, including deposits and trading, will be disabled. If you encounter any problems
 with the withdrawal function, please contact Binance Customer Support as soon as possible.
    3. Resetting your certification affects every step of your account verification. You will need to re-provide all the 
information required for the new process. Please confirm the need for resetting.
''',
        )
        bot.send_message(user_id, " Select the reason why you want to update your KYC:")
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("The documents have expired.", callback_data='1')
        button2 = types.InlineKeyboardButton("Update your country of residence", callback_data='2')
        button3 = types.InlineKeyboardButton("Name changed in documents", callback_data='3')
        button4 = types.InlineKeyboardButton("Code changed in documents", callback_data='4')
        button5 = types.InlineKeyboardButton("Nationality changed", callback_data='5')
        button6 = types.InlineKeyboardButton("Updating documents for using the fiat channel.", callback_data='6')
        button7 = types.InlineKeyboardButton("Update documents according to Binance Card requirements", callback_data='7')
        markup.add(button1, button2, button3,button4,button5,button6,button7)
        bot.send_message(message.chat.id, "Choose one button:", reply_markup=markup)
    if message.text=="Change of residence your address":
        bot.send_message(user_id, "Please enter your  new address:")
        user_state[user_id] = "waiting_for_new_address"
    if message.text=="Appealing KYC rejection":
        bot.send_message(user_id, "Write why Appealing your KYC rejection:?")
        user_state[user_id] = "waiting_for_new_appealing"
    if message.text=="Write to support":
        bot.send_message(user_id, "Write command /WriteToSupport (YOUR Problem) ")
if __name__=="__main__":
    bot.infinity_polling()