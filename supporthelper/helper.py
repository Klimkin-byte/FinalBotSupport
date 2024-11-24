
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
    list_emails=reademail()
    print(old_email)
    if old_email in list_emails:
        list_emails=[new_email if email == old_email else email for email in list_emails]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_emails))
        print("Email changes!")
    else:
        print("no email.")

def pass_changes(old_pass,new_pass):
    list_pass=reademail()
    if old_pass in list_pass:
        list_pass=[new_pass if password == old_pass else password for password in list_pass]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_pass))
        print("Password changes!")
    else:
        print("no password.")

def fa_email():
    list_fa = reademail()
    if "2FAE-True" in list_fa:
        list_fa=["2FAE-False" if fa_mail == "2FAE-True" else fa_mail for fa_mail in list_fa]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa))
            print("Email fa changes!")
    else:
        list_fa = ["2FAE-True" if fa_mail == "2FAE-False" else fa_mail for fa_mail in list_fa]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa))
            print("Email fa changes!")

def fa_number():
    list_number = reademail()
    if "2FAN-True" in list_number:
        list_fa=["2FAN-False" if fa_mail == "2FAN-True" else fa_mail for fa_mail in list_number]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa))
            print("number fa changes!")
    else:
        list_fa = ["2FAN-True" if fa_mail == "2FAN-False" else fa_mail for fa_mail in list_number]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa))
            print("number fa changes!")

def fa_app():
    list_app = reademail()
    if "2FAA-True" in list_app:
        list_fa=["2FAA-False" if fa_mail == "2FAA-True" else fa_mail for fa_mail in list_app]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa))
            print("number fa changes!")
    else:
        list_fa = ["2FAA-True" if fa_mail == "2FAA-False" else fa_mail for fa_mail in list_app]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa))
            print("number fa changes!")

def fa_key():
    list_key = reademail()
    if "2FAK-True" in list_key:
        list_fa=["2FAK-False" if fa_mail == "2FAK-True" else fa_mail for fa_mail in list_key]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa))
            print("number fa changes!")
    else:
        list_fa = ["2FAK-True" if fa_mail == "2FAK-False" else fa_mail for fa_mail in list_key]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa))
            print("number fa changes!")


def new_name(user_name_reset): ###нужно постоянно менять имя так как не получаем данных с базы данных
    list_name = reademail()
    if "Masik" in list_name:
        list_fa_name=[user_name_reset if fa_mail == "Masik" else fa_mail for fa_mail in list_name]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa_name))
            print("number fa changes!")
    else:
        print("no name")

def new_date(user_date_reset): ###нужно постоянно менять date
    list_date = reademail()
    if "13.10.2015" in list_date:
        list_fa_name = [user_date_reset if fa_mail == "13.10.2015" else fa_mail for fa_mail in list_date]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa_name))
            print("number fa changes!")
    else:
        print("no date")

def reactivation():
    list_reactivation = reademail()
    if "Account-True" in list_reactivation:
        list_fa = ["Account-False" if fa_mail == "Account-True" else fa_mail for fa_mail in list_reactivation]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa))
            print("reactivation reset!")

    else:
        list_fa = ["Account-False" if fa_mail == "Account-False" else fa_mail for fa_mail in list_reactivation]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa))
            print("reactivation reset!")

def inheritance_data(data,user_id):
    list_data=reademail_name()
    list_data.append(data)
    list_data.append(str(user_id))
    with open("C:/Users/Dreimond/Desktop/inpython.txt", "w", encoding='utf-8') as file_slov:
        file_slov.write(" ".join(list_data))
        print("reactivation reset!")
        print(list_data)

def activating_acc():
    list_reactivation = reademail()
    if "Activating-False" in list_reactivation:
        list_fa = ["Activating-True" if fa_mail == "Activating-False" else fa_mail for fa_mail in list_reactivation]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa))
            print("reactivation reset!")
    else:
        print("was activating")

def handle_photo(downloaded_file,file_name):
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

def kys_reset_types(answer_callback):
    list_reset_kys = reademail()
    if "KYSRESET-False" in list_reset_kys:
        list_fa = [answer_callback if fa_mail == "KYSRESET-False" else fa_mail for fa_mail in list_reset_kys]
        with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
            file_slov.write(" ".join(list_fa))
            file_slov.write(" KYSRESET-False")
            print("KYS reset!")
    else:
        print("was reset")

def new_address(user_new_address):
    list_reset_kys = reademail()
    with open("C:/Users/Dreimond/Desktop/outpython.txt", "w", encoding='utf-8') as file_slov:
        file_slov.write(" ".join(list_reset_kys))
        file_slov.write(" ")
        file_slov.write(user_new_address)
        print("new address")

def user_problem_appealing(user_appealing_text, user_id):
    list_appealing=reademail_appealing()
    list_appealing.append(user_appealing_text)
    list_appealing.append(str(user_id))
    with open("C:/Users/Dreimond/Desktop/whyme.txt", "a", encoding='utf-8') as file_slov:
        file_slov.write(" ".join(list_appealing))
        file_slov.write("\n")
        print("apellianing correct!")
        print(list_appealing)
