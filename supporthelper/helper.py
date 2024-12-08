#from data_base.data_base_users import *
import sqlite3
from data_base.data_base_users import Database

db = Database("C:/Users/Dreimond/PycharmProjects/FinalBotSupport/data_base/database.db")
email_for_function=[]

def email_for_all(old_email):
    email_for_function.append(old_email)

def reademail():
    try:
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "r", encoding='utf-8') as file_slov:
            file_read=file_slov.read()
            list_text=file_read.split()
        return list_text
    except FileNotFoundError:
        return ""

def reademail_name():
    try:
        with open("C:/Users/Dreimond/Desktop/inpython.txt", "r", encoding='utf-8') as file_text:
            file_read=file_text.read()
            list_text=file_read.split()
        return list_text
    except FileNotFoundError:
        return ""

def reademail_appealing():
    try:
        with open("C:/Users/Dreimond/Desktop/whyme.txt", "r", encoding='utf-8') as file_text:
            file_read=file_text.read()
            list_text=file_read.split()
        return list_text
    except FileNotFoundError:
        return ""

def changes(new_email,old_email):
    updated_rows = db.update_user_field(old_email, "email", new_email)
    if updated_rows:
        print("Update.")
    else:
        print("not find.")
    return new_email


def pass_changes(user_new_password,old_email):
    updated_rows = db.update_user_field(old_email, "password", user_new_password)
    if updated_rows:
        print("Update.")
    else:
        print("not find.")

def fa_email(old_email):
    check_data1 = {"two_factor_ae":"False"}
    print(check_data1)
    print(old_email)
    if db.check_multiple_conditions(check_data1):
        updated_rows = db.update_user_field(old_email, "two_factor_ae", "True")
        if updated_rows:
            print("Update1.")
        else:
            print("not find.")
    else:
        updated_rows = db.update_user_field(old_email, "two_factor_ae", "False")
        if updated_rows:
            print("Update2.")
        else:
            print("not find.")

def fa_number(old_email):
    check_data = {"two_factor_an":"True"}
    if db.check_multiple_conditions(check_data):
        updated_rows = db.update_user_field(old_email, "two_factor_an", "False")
        if updated_rows:
            print("Update1.")
        else:
            print("not find.")
    else:
        updated_rows = db.update_user_field(old_email, "two_factor_an", "True")
        if updated_rows:
            print("Update2.")
        else:
            print("not find.")


def fa_app(old_email):
    check_data = {"two_factor_aa": "False"}
    if db.check_multiple_conditions(check_data):
        updated_rows = db.update_user_field(old_email, "two_factor_aa", "True")
        if updated_rows:
            print("Update1.")
        else:
            print("not find.")
    else:
        updated_rows = db.update_user_field(old_email, "two_factor_aa", "False")
        if updated_rows:
            print("Update2.")
        else:
            print("not find.")

def fa_key(old_email):
    check_data = {"two_factor_ak": "False"}
    if db.check_multiple_conditions(check_data):
        updated_rows = db.update_user_field(old_email, "two_factor_ak", "True")
        if updated_rows:
            print("Update1.")
        else:
            print("not find.")
    else:
        updated_rows = db.update_user_field(old_email, "two_factor_ak", "False")
        if updated_rows:
            print("Update2.")
        else:
            print("not find.")


def new_name(user_name_reset,old_email):
    updated_rows = db.update_user_field(old_email, "name", user_name_reset)
    if updated_rows:
        print("Update.")
    else:
        print("not find.")

def new_date(user_date_reset,old_email):
    updated_rows = db.update_user_field(old_email, "date", user_date_reset)
    if updated_rows:
        print("Update.")
    else:
        print("not find.")

def reactivation(old_email):
    check_data = {"Account": "True"}
    if db.check_multiple_conditions(check_data):
        updated_rows = db.update_user_field(old_email, "Account", "False")
        if updated_rows:
            print("Update.")
        else:
            print("not find.")
    else:
        updated_rows = db.update_user_field(old_email, "Account", "False")
        if updated_rows:
            print("Update.")
        else:
            print("not find.")

def inheritance_data(data,user_id):
    list_data=reademail_name()
    list_data.append(data)
    list_data.append(str(user_id))
    with open("C:/Users/Dreimond/Desktop/inpython.txt", "w", encoding='utf-8') as file_slov:
        file_slov.write(" ".join(list_data))
        print("reactivation reset!")
        print(list_data)

def activating_acc(old_email):
    check_data = {"Activating": "False"}
    if db.check_multiple_conditions(check_data):
        updated_rows = db.update_user_field(old_email, "Account", "True")
        if updated_rows:
            print("Update.")
        else:
            print("reactivation reset!")
    else:
        print("was activating")

def handle_photo(downloaded_file,file_name):
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

def kys_reset_types(answer_callback):
    data="".join(email_for_function)
    print(data)
    check_data = {"KYSREST": "False"}
    if db.check_multiple_conditions(check_data):
        updated_rows1 = db.update_user_field(data, "KYSREST", "False")
        updated_rows = db.update_user_field(data, "KYSDATA", answer_callback)
        if updated_rows and updated_rows1:
            print("Update.")
        else:
            print("reactivation reset!")
    else:
        print("was reset")

def new_address(user_new_address):
    data="".join(email_for_function)
    updated_rows = db.update_user_field(data, "PersonAdress", user_new_address)
    if updated_rows:
        print("Update.")
    else:
        print("reactivation reset!")


def user_problem_appealing(user_appealing_text, user_id):
    list_appealing=reademail_appealing()
    list_appealing.append(user_appealing_text)
    list_appealing.append(str(user_id))
    with open("C:/Users/Dreimond/Desktop/whyme.txt", "a", encoding='utf-8') as file_slov:
        file_slov.write(" ".join(list_appealing))
        file_slov.write("\n")
        print("apellianing correct!")
        print(list_appealing)

