import pytest
from unittest.mock import MagicMock,call
from supporthelper.helper import *
import os


def test_reademail_name():
    assert reademail_name()!=[]

def test_reademail_appealing():
    assert reademail_appealing()!=[]


def changes_email(new_email, old_email, db):
    updated_rows = db.update_user_field(old_email, "email", new_email)
    if updated_rows:
        print("Update.")
    else:
        print("Not found.")


def test_changes_update():
    mock_db = MagicMock()
    mock_db.update_user_field.return_value = 1
    changes_email("newemail@example.com", "oldemail@example.com", mock_db)
    mock_db.update_user_field.assert_called_once_with("oldemail@example.com", "email", "newemail@example.com")

def test_changes_not_found():
    mock_db = MagicMock()
    mock_db.update_user_field.return_value = 0
    changes_email("newemail@example.com", "nonexistentemail@example.com", mock_db)
    mock_db.update_user_field.assert_called_once_with("nonexistentemail@example.com", "email", "newemail@example.com")


def changes_pass(new_pass, old_email, dt):
    updated_rows = dt.update_user_field(old_email, "password", new_pass)
    if updated_rows:
        print("Update.")
    else:
        print("Not found.")


def test_changes_update_pass():
    mock_dt = MagicMock()
    mock_dt.update_user_field.return_value = 1
    changes_pass("new_pass", "old_email", mock_dt)
    mock_dt.update_user_field.assert_called_once_with("old_email", "password", "new_pass")
def test_changes_not_found_pass():
    mock_dt = MagicMock()
    mock_dt.update_user_field.return_value = 0
    changes_pass("new_pass", "old_email", mock_dt)
    mock_dt.update_user_field.assert_called_once_with("old_email", "password", "new_pass")



def fa_changes_email(old_email,db):
    check_data = {"two_factor_ae": "True"}
    if db.check_multiple_conditions(check_data):
        updated_rows = db.update_user_field(old_email, "two_factor_ae", "False")
        if updated_rows:
            print("Update.")
        else:
            print("Not found.")
    else:
        updated_rows = db.update_user_field(old_email, "two_factor_ae", "True")
        if updated_rows:
            print("Update.")
        else:
            print("Not found.")

def test_changes_fa_email():
    mock_dt = MagicMock()
    mock_dt.update_user_field.return_value = 1
    fa_changes_email("old_email", mock_dt)
    check_data = {"two_factor_ae": "True"}
    if db.check_multiple_conditions(check_data):
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_ae", "False")
    else:
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_ae", "True")
def test_changes_not_fa_email():
    mock_dt = MagicMock()
    mock_dt.update_user_field.return_value = 0
    fa_changes_email("old_email", mock_dt)
    check_data = {"two_factor_ae": "True"}
    if db.check_multiple_conditions(check_data):
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_ae", "False")
    else:
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_ae", "True")

def fa_changes_number(old_email,db):
    check_data = {"two_factor_ae": "True"}
    if db.check_multiple_conditions(check_data):
        updated_rows = db.update_user_field(old_email, "two_factor_an", "False")
        if updated_rows:
            print("Update.")
        else:
            print("Not found.")
    else:
        updated_rows = db.update_user_field(old_email, "two_factor_an", "True")
        if updated_rows:
            print("Update.")
        else:
            print("Not found.")


def test_changes_fa_number():
    mock_dt = MagicMock()
    mock_dt.update_user_field.return_value = 1
    fa_changes_number("old_email", mock_dt)
    check_data = {"two_factor_an": "True"}
    if db.check_multiple_conditions(check_data):
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_an", "False")
    else:
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_an", "True")
def test_changes_not_fa_number():
    mock_dt = MagicMock()
    mock_dt.update_user_field.return_value = 0
    fa_changes_number("old_email", mock_dt)
    check_data = {"two_factor_an": "True"}
    if db.check_multiple_conditions(check_data):
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_an", "False")
    else:
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_an", "True")




def fa_changes_app(old_email,db):
    check_data = {"two_factor_aa": "True"}
    if db.check_multiple_conditions(check_data):
        updated_rows = db.update_user_field(old_email, "two_factor_aa", "False")
        if updated_rows:
            print("Update.")
        else:
            print("Not found.")
    else:
        updated_rows = db.update_user_field(old_email, "two_factor_aa", "True")
        if updated_rows:
            print("Update.")
        else:
            print("Not found.")

def test_changes_fa_app():
    mock_dt = MagicMock()
    mock_dt.update_user_field.return_value = 1
    fa_changes_app("old_email", mock_dt)
    check_data = {"two_factor_aa": "True"}
    if db.check_multiple_conditions(check_data):
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_aa", "False")
    else:
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_aa", "True")
def test_changes_not_fa_app():
    mock_dt = MagicMock()
    mock_dt.update_user_field.return_value = 0
    fa_changes_app("old_email", mock_dt)
    check_data = {"two_factor_aa": "True"}
    if db.check_multiple_conditions(check_data):
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_aa", "False")
    else:
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_aa", "True")


###
def fa_changes_key(old_email,db):
    check_data = {"two_factor_ak": "True"}
    if db.check_multiple_conditions(check_data):
        updated_rows = db.update_user_field(old_email, "two_factor_ak", "False")
        if updated_rows:
            print("Update.")
        else:
            print("Not found.")
    else:
        updated_rows = db.update_user_field(old_email, "two_factor_ak", "True")
        if updated_rows:
            print("Update.")
        else:
            print("Not found.")

def test_changes_fa_key():
    mock_dt = MagicMock()
    mock_dt.update_user_field.return_value = 1
    fa_changes_key("old_email", mock_dt)
    check_data = {"two_factor_ak": "True"}
    if db.check_multiple_conditions(check_data):
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_ak", "False")
    else:
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_ak", "True")
def test_changes_not_fa_key():
    mock_dt = MagicMock()
    mock_dt.update_user_field.return_value = 0
    fa_changes_key("old_email", mock_dt)
    check_data = {"two_factor_aa": "True"}
    if db.check_multiple_conditions(check_data):
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_ak", "False")
    else:
        mock_dt.update_user_field.assert_called_once_with("old_email", "two_factor_ak", "True")


####
def new_changes_name(user_name_reset, old_email, db):
    updated_rows = db.update_user_field(old_email, "name", user_name_reset)
    if updated_rows:
        print("Update.")
    else:
        print("Not found.")

def test_changes_name():
    mock_db = MagicMock()
    mock_db.update_user_field.return_value = 1
    new_changes_name("Vasya", "oldemail@example.com", mock_db)
    mock_db.update_user_field.assert_called_once_with("oldemail@example.com", "name", "Vasya")

def test_changes_not_name():
    mock_db = MagicMock()
    mock_db.update_user_field.return_value = 0
    new_changes_name("Vasya", "nonexistentemail@example.com", mock_db)
    mock_db.update_user_field.assert_called_once_with("nonexistentemail@example.com", "name", "Vasya")

###date
def new_changes_date(user_date_reset, old_email, db):
    updated_rows = db.update_user_field(old_email, "date", user_date_reset)
    if updated_rows:
        print("Update.")
    else:
        print("Not found.")

def test_changes_date():
    mock_db = MagicMock()
    mock_db.update_user_field.return_value = 1
    new_changes_date("10.12.1999", "oldemail@example.com", mock_db)
    mock_db.update_user_field.assert_called_once_with("oldemail@example.com", "date", "10.12.1999")

def test_changes_not_date():
    mock_db = MagicMock()
    mock_db.update_user_field.return_value = 0
    new_changes_date("10.12.1999", "nonexistentemail@example.com", mock_db)
    mock_db.update_user_field.assert_called_once_with("nonexistentemail@example.com", "date", "10.12.1999")

####reactiv

def changes_reactivation(old_email,db):
    check_data = {"Account": "True"}
    if db.check_multiple_conditions(check_data):
        updated_rows = db.update_user_field(old_email, "Account", "False")
        if updated_rows:
            print("Update.")
        else:
            print("Not found.")
    else:
        updated_rows = db.update_user_field(old_email, "Account", "True")
        if updated_rows:
            print("Update.")
        else:
            print("Not found.")

def test_changes_reactivation():
    mock_dt = MagicMock()
    mock_dt.update_user_field.return_value = 1
    changes_reactivation("old_email", mock_dt)
    check_data = {"Account": "False"}
    if db.check_multiple_conditions(check_data):
        mock_dt.update_user_field.assert_called_once_with("old_email", "Account", "False")
    else:
        mock_dt.update_user_field.assert_called_once_with("old_email", "Account", "True")
def test_changes_no_reactivation():
    mock_dt = MagicMock()
    mock_dt.update_user_field.return_value = 0
    changes_reactivation("old_email", mock_dt)
    check_data = {"Account": "False"}
    if db.check_multiple_conditions(check_data):
        mock_dt.update_user_field.assert_called_once_with("old_email", "Account", "False")
    else:
        mock_dt.update_user_field.assert_called_once_with("old_email", "Account", "True")

TEST_FILE_PATH = "C:/Users/Dreimond/Desktop/inpython.txt"


def reademail_name_mock(existing_content):
    try:
        with open(TEST_FILE_PATH, "r", encoding="utf-8") as file_text:
            file_read = file_text.read()
            list_text = file_read.split()
        return list_text
    except FileNotFoundError:
        return []


def inheritance_data_test(data, user_id):
    list_data = reademail_name_mock([])
    list_data.append(data)
    list_data.append(str(user_id))
    with open(TEST_FILE_PATH, "w", encoding="utf-8") as file_slov:
        file_slov.write(" ".join(list_data))
    return " ".join(list_data)


@pytest.fixture
def prepare_file():
    if os.path.exists(TEST_FILE_PATH):
        with open(TEST_FILE_PATH, "w", encoding="utf-8") as file:
            file.truncate(0)  # Очищает содержимое файла, не удаляя его.
    yield


def test_inheritance_data_file_not_found(prepare_file):
    result = inheritance_data_test("Some info", "1234")
    expected = "Some info 1234"
    assert result == expected
    with open(TEST_FILE_PATH, "r", encoding="utf-8") as file:
        file_content = file.read()
    assert file_content == expected

def test_inheritance_data_with_existing_file(prepare_file):
    with open(TEST_FILE_PATH, "w", encoding="utf-8") as file:
        file.write("existing data")
    result = inheritance_data_test("New info", "5678")
    expected = "existing data New info 5678"
    assert result == expected
    with open(TEST_FILE_PATH, "r", encoding="utf-8") as file:
        file_content = file.read()
    assert file_content == expected

###activating

def change_activating_acc(old_email,db):
    check_data = {"Activating": "False"}
    if db.check_multiple_conditions(check_data):
        updated_rows = db.update_user_field(old_email, "Activating", "True")
        if updated_rows:
            print("Update.")
        else:
            print("Not found.")
    else:
        print("Was active.")

def test_changes_activating_acc():
    mock_db = MagicMock()
    mock_db.update_user_field.return_value = 1
    change_activating_acc( "oldemail@example.com", mock_db)
    mock_db.update_user_field.assert_called_once_with("oldemail@example.com", "Activating", "True")

def test_changes_not_activating_acc():
    mock_db = MagicMock()
    mock_db.update_user_field.return_value = 0
    change_activating_acc("nonexistentemail@example.com", mock_db)
    mock_db.update_user_field.assert_called_once_with("nonexistentemail@example.com", "Activating", "True")


###
@pytest.fixture
def cleanup_test_file():
    test_file_name = "test_image.jpg"
    yield test_file_name
    if os.path.exists(test_file_name):
        os.remove(test_file_name)
def test_handle_photo(cleanup_test_file):
    test_data = b"binary_image_data"
    file_name = cleanup_test_file
    handle_photo(test_data, file_name)
    assert os.path.exists(file_name), "Файл не был создан"
def test_handle_photo_file(cleanup_test_file):
    test_data = b"binary_image_data"
    file_name = cleanup_test_file
    handle_photo(test_data, file_name)
    with open(file_name, "rb") as f:
        saved_data = f.read()
    assert saved_data == test_data, "Содержимое файла не совпадает с ожидаемым"
def test_handle_photo_overwrites_file(cleanup_test_file):

    initial_data = b"old_data"
    new_data = b"new_data"
    file_name = cleanup_test_file
    # Создаём файл с начальными данными
    with open(file_name, "wb") as f:
        f.write(initial_data)
    # Вызываем функцию для перезаписи
    handle_photo(new_data, file_name)
    # Проверяем содержимое файла
    with open(file_name, "rb") as f:
        saved_data = f.read()
    assert saved_data == new_data, "Файл не был перезаписан корректно"
#####
def change_kys_rest(old_email,answer_callback,db):
    check_data = {"KYSREST": "False"}
    if db.check_multiple_conditions(check_data):
        updated_rows1 = db.update_user_field(old_email, "KYSREST", "False")
        updated_rows = db.update_user_field(old_email, "KYSDATA", answer_callback)
        if updated_rows and updated_rows1:
            print("Update.")
        else:
            print("Not found.")
    else:
        print("Was active.")

def test_change_kys_rest():
    mock_db = MagicMock()
    mock_db.update_user_field.return_value = 1
    mock_db.update_user_field.side_effect = [1, 1]
    change_kys_rest( "oldemail@example.com","answer_callback", mock_db)
    mock_db.check_multiple_conditions.assert_called_once_with({"KYSREST": "False"})
    mock_db.update_user_field.assert_has_calls([
        call("oldemail@example.com", "KYSREST", "False"),
        call("oldemail@example.com", "KYSDATA", "answer_callback")
    ])
    assert mock_db.update_user_field.call_count == 2

def test_change_kys_no_rest():
    mock_db = MagicMock()
    mock_db.check_multiple_conditions.return_value = 1
    mock_db.update_user_field.side_effect = [0, 0]
    change_kys_rest("nonexistentemail@example.com", "answer_callback", mock_db)
    mock_db.check_multiple_conditions.assert_called_once_with({"KYSREST": "False"})
    mock_db.update_user_field.assert_has_calls([
        call("nonexistentemail@example.com", "KYSREST", "False"),
        call("nonexistentemail@example.com", "KYSDATA", "answer_callback")
    ])
    assert mock_db.update_user_field.call_count == 2
####
def changes_person_adress(new_adress, old_email, db):
    updated_rows = db.update_user_field(old_email, "PersonAdress", new_adress)
    if updated_rows:
        print("Update.")
    else:
        print("Not found.")

def test_changes_person_adress():
    mock_db = MagicMock()
    mock_db.update_user_field.return_value = 1
    changes_person_adress("ODessa Deribasovskaya", "oldemail@example.com", mock_db)
    mock_db.update_user_field.assert_called_once_with("oldemail@example.com", "PersonAdress", "ODessa Deribasovskaya")

def test_changes_no_person_adress():
    mock_db = MagicMock()
    mock_db.update_user_field.return_value = 0
    changes_person_adress("ODessa Deribasovskaya", "nonexistentemail@example.com", mock_db)
    mock_db.update_user_field.assert_called_once_with("nonexistentemail@example.com", "PersonAdress", "ODessa Deribasovskaya")

#####
TEST_FILE_PATH2 = "C:/Users/Dreimond/Desktop/whyme.txt"
def appealing_name_mock(existing_content):
    try:
        with open(TEST_FILE_PATH2, "r", encoding="utf-8") as file_text:
            file_read = file_text.read()
            list_text = file_read.split()
        return list_text
    except FileNotFoundError:
        return []

def appealing_data_test(user_appealing_text, user_id):
    list_data = reademail_name_mock([])
    list_data.append(user_appealing_text)
    list_data.append(str(user_id))
    with open(TEST_FILE_PATH2, "w", encoding="utf-8") as file_slov:
        file_slov.write(" ".join(list_data))
    return " ".join(list_data)


@pytest.fixture
def prepare_file_appealing():
    if os.path.exists(TEST_FILE_PATH):
        with open(TEST_FILE_PATH2, "w", encoding="utf-8") as file:
            file.truncate(0)  # Очищает содержимое файла, не удаляя его.
    yield

def appealing_data_file_not_found(prepare_file_appealing):
    result = appealing_data_test("Some info", "1234")
    expected = "Some info 1234"
    assert result == expected
    with open(TEST_FILE_PATH2, "r", encoding="utf-8") as file:
        file_content = file.read()
    assert file_content == expected

def appealing_data_with_existing_file(prepare_file_appealing):
    with open(TEST_FILE_PATH2, "w", encoding="utf-8") as file:
        file.write("existing data")
    result = appealing_data_test("New info", "5678")
    expected = "existing data New info 5678"
    assert result == expected
    with open(TEST_FILE_PATH2, "r", encoding="utf-8") as file:
        file_content = file.read()
    assert file_content == expected