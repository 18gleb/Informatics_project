from random import choice, randint

from CRUD import found_word_on_rus_in_liberty_using_user_id, found_word_on_rus_in_database, add_word_in_liberty_word, \
    found_word_on_eng_in_database, found_word_on_eng_in_liberty_using_user_id, get_nikname, get_phone, get_mail, \
    get_password, get_words, get_not_studied_words, found_all_words_in_liberty, get_studied_words
from exceptions import IncorrectPhoneNumber, IncorrectLenPhoneNumber, IncorrectMail, NumberNotFound, \
    WordAlreadyInLiberty, WordNotInDatabase, WordDoesNotExist, ShortPassword
from qt.lesson1 import Lesson1
from qt.lesson2 import Lesson2
from qt.lesson3 import Lesson3


def check_mail_or_phone(mail_or_phone: str):
    phone = None
    mail = None
    if len(mail_or_phone) == 0:
        return NumberNotFound()
    if mail_or_phone[0] == "8" or mail_or_phone[0:2:] == "+7":
        if mail_or_phone[0:2:] == "+7":
            mail_or_phone = "8" + mail_or_phone[2::]
        phone = mail_or_phone
    else:
        mail = mail_or_phone
    if mail is None:
        if len(phone) != 11:
            return IncorrectLenPhoneNumber()
        try:
            phone = int(phone)
        except ValueError:
            return IncorrectPhoneNumber()
        return "phone", phone
    else:
        dog = 0
        rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя&=+<>,_'-"
        for i in range(0, len(mail)):
            if mail[i].lower() in rus:
                return IncorrectMail()
            elif mail[i] == "@":
                dog += 1
                if dog > 1:
                    return IncorrectMail()
        if dog == 0:
            return IncorrectMail()
        if ".." in mail:
            return IncorrectMail()
        return "mail", mail


def check_word_in_liberty(word: str, user_id: int):
    rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    eng = "abcdefghijklmnopqrstuvwxyz"
    count_rus = 0
    count_eng = 0
    for i in word:
        if i.lower() in eng:
            count_eng += 1
        elif i.lower() in rus:
            count_rus += 1
    if len(word) == count_rus:
        if found_word_on_rus_in_database(word):
            if found_word_on_rus_in_liberty_using_user_id(user_id, word):
                print("daddda")
                add_word_in_liberty_word(user_id, word)
                print("Слово успешно добавлено")
                return "Ок"
            else:
                print("Это слово уже есть в вашей библиотеке")
                return WordAlreadyInLiberty()
        else:
            print("К сожалению этого слова нет в нашей базе, но мы обязательно его добавим")
            return WordNotInDatabase()
    elif len(word) == count_eng:
        if found_word_on_eng_in_database(word):
            if found_word_on_eng_in_liberty_using_user_id(user_id, word):
                add_word_in_liberty_word(user_id, word)
                print("Слово успешно добавлено")
                return "Ок"
            else:
                print("Это слово уже есть в вашей библиотеке")
                return WordAlreadyInLiberty()
        else:
            print("К сожалению этого слова нет в нашей базе, но мы обязательно его добавим")
            return WordNotInDatabase()
    else:
        print("Такое слово не существует")
        return WordDoesNotExist()


def update_my_liberty(user_id: int, page):
    page.output_nikname.setText(get_nikname(user_id))
    if get_phone(user_id) is None:
        page.output_phone.setStyleSheet("color: rgb(255, 140, 0)")
        page.output_phone.setText("Вы не добавили номер телефона")
    else:
        page.output_phone.setStyleSheet("color: rgb(0, 0, 0)")
        page.output_phone.setText(get_phone(user_id))
    if get_mail(user_id) is None:
        page.output_mail.setStyleSheet("color: rgb(255, 140, 0)")
        page.output_mail.setText("Вы не добавили адрес электронной почты")
    else:
        page.output_mail.setStyleSheet("color: rgb(0, 0, 0)")
        page.output_mail.setText(get_mail(user_id))
    page.output_password.setText("*" * len(get_password(user_id)))


def check_password(password: str):
    if len(password) < 8:
        return ShortPassword()
    else:
        return "Ок"


def create_training(user_id):
    training = []
    words = get_not_studied_words(user_id)
    if len(words) >= 5:
        words_for_training = []
        for i in range(0, 5):
            words_for_training.append(choice(words))
        count_les1 = randint(1, 2)
        count_les2 = randint(1, 2)
        count_les3 = 5 - count_les2 - count_les1
        for j in range(0, count_les1):
            correct_word = choice(words_for_training)
            words_for_training.remove(correct_word)
            training.append(Lesson1(correct_word))
        for w in range(0, count_les2):
            correct_word = choice(words_for_training)
            words_for_training.remove(correct_word)
            training.append(Lesson2(correct_word))
        for g in range(0, count_les3):
            correct_word = choice(words_for_training)
            words_for_training.remove(correct_word)
            training.append(Lesson3(words, correct_word))
    else:
        lessons = [Lesson2, Lesson1]
        for k in range(0, len(words)):
            lesson = choice(lessons)
            correct_word = choice(words)
            words.remove(correct_word)
            training.append(lesson(correct_word))
    return training

