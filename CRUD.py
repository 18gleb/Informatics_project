from data_base import session_factory, User, Liberty, Word, Liberty_word


def create_User(mail, phone, password, nickname):
    session = session_factory()
    user = User(mail=mail, phone=phone, password=password, nickname=nickname)
    session.add(user)
    session.commit()
    user_id = session.query(User).where(User.nickname == nickname).first()
    user_id = user_id.id
    liberty = Liberty(user_id=user_id)
    session.add(liberty)
    session.commit()
    session.close()


def get_by_field_user(phone):
    session = session_factory()
    user = session.query(User).group_by(User.phone).all()
    session.close()
    return User


def update_user():
    session = session_factory()
    user = session.query(User).where(User.id == 1).first()
    user.phone = user.phone
    session.commit()
    session.close()


def delete_user():
    session = session_factory()
    user = session.query(User).where(User.id == 1).first()
    session.delete(user)
    session.commit()
    session.close()


def create_Liberty(user_id):
    session = session_factory()
    liberty = Liberty(user_id=user_id)
    session.add(liberty)
    session.commit()
    session.close()


def get_by_field_liberty(id):
    session = session_factory()
    liberty = session.query(Liberty).group_by(Liberty.id).all()
    session.close()
    return Liberty


def update_liberty():
    session = session_factory()
    liberty = session.query(Liberty).where(Liberty.id == 1).first()
    liberty.id = liberty.id
    session.commit()
    session.close()


def delete_liberty():
    session = session_factory()
    liberty = session.query(Liberty).where(Liberty.id == 1).first()
    session.delete(liberty)
    session.commit()
    session.close()


def create_Word(on_rus, on_eng, how_to_listen, type_id):
    session = session_factory()
    word = Word(on_rus=on_rus, on_eng=on_eng, how_to_listen=how_to_listen, type_id=type_id)
    session.add(word)
    session.commit()
    session.close()


def get_by_field_word(word_id):
    session = session_factory()
    word = session.query(Word).where(Word.id == word_id).first()
    session.close()
    return word


def update_word():
    session = session_factory()
    word = session.query(Word).where(Word.id == 1).first()
    word.id = word.id
    session.commit()
    session.close()


def delete_word():
    session = session_factory()
    word = session.query(Word).where(Word.id == 1).first()
    session.delete(word)
    session.commit()
    session.close()


def create_liberty_word(liberty_id, word_id, true_or_false):
    session = session_factory()
    liberty_word = Liberty_word(liberty_id=liberty_id, word_id=word_id, true_or_false=true_or_false)
    session.add(liberty_word)
    session.commit()
    session.close()


def get_by_field_liberty_word(liberty_id):
    session = session_factory()
    liberty_word = session.query(Liberty_word).group_by(Liberty_word.liberty_id).all()
    session.close()
    return liberty_word


def delete_liberty_word():
    session = session_factory()
    liberty_word = session.query(Liberty_word).where(Liberty_word.liberty_id == 1).first()
    session.delete()
    session.commit()
    session.close()


def check_nikname(nikname: str):
    session = session_factory()
    user = session.query(User).where(User.nickname == nikname).first()
    session.close()
    if user is not None:
        return False
    else:
        return True


def found_user_using_phone(phone):
    session = session_factory()
    user = session.query(User).where(User.phone == str(phone)).first()
    session.close()
    return user


def found_user_using_mail(mail):
    session = session_factory()
    user = session.query(User).where(User.mail == mail).first()
    session.close()
    return user


def found_all_words_in_liberty(user_id):
    session = session_factory()
    liberty = session.query(Liberty).where(Liberty.user_id == user_id).first()
    liberty_words = session.query(Liberty_word).where(Liberty_word.liberty_id == liberty.id).all()
    session.close()
    return len(liberty_words)


def found_word_on_rus_in_liberty_using_user_id(user_id: int, wor: str):
    session = session_factory()
    liberty = session.query(Liberty).where(Liberty.user_id == user_id).first()
    word = session.query(Word).where(Word.on_rus == wor).first()
    liberty_word = session.query(Liberty_word).where(Liberty_word.liberty_id == liberty.id,
                                                     Liberty_word.word_id == word.id).first()
    if liberty_word:
        session.close()
        return False
    else:
        session.close()
        return True


def found_word_on_rus_in_database(word: str):
    session = session_factory()
    word = session.query(Word).where(Word.on_rus == word).first()
    if word is not None:
        session.close()
        return True
    else:
        session.close()
        return False


def add_word_in_liberty_word(user_id: int, word: str):
    session = session_factory()
    liberty = session.query(Liberty).where(Liberty.user_id == user_id).first()
    word_on_rus = session.query(Word).where(Word.on_rus == word).first()
    if word_on_rus is None:
        word_on_eng = session.query(Word).where(Word.on_eng == word).first()
        create_liberty_word(liberty.id, word_on_eng.id, False)
        session.close()
    else:
        create_liberty_word(liberty.id, word_on_rus.id, False)
        session.close()


def found_word_on_eng_in_database(word: str):
    session = session_factory()
    word = session.query(Word).where(Word.on_eng == word).first()
    if word is not None:
        session.close()
        return True
    else:
        session.close()
        return False


def found_word_on_eng_in_liberty_using_user_id(user_id: int, wor: str):
    session = session_factory()
    liberty = session.query(Liberty).where(Liberty.user_id == user_id).first()
    word = session.query(Word).where(Word.on_eng == wor).first()
    liberty_word = session.query(Liberty_word).where(Liberty_word.liberty_id == liberty.id,
                                                     Liberty_word.word_id == word.id).first()
    if liberty_word:
        session.close()
        return False
    else:
        session.close()
        return True


def get_words(user_id: int):
    session = session_factory()
    liberty = session.query(Liberty).where(Liberty.user_id == user_id).first()
    liberty_words = session.query(Liberty_word).where(Liberty_word.liberty_id == liberty.id).all()
    words = []
    if liberty_words:
        for i in liberty_words:
            words.append(session.query(Word).where(Word.id == i.word_id).first())
    session.close()
    return words


def del_word_in_liberty_word(user_id: int, word: str):
    session = session_factory()
    liberty = session.query(Liberty).where(Liberty.user_id == user_id).first()
    word = session.query(Word).where(Word.on_rus == word).first()
    liberty_word = session.query(Liberty_word).where(Liberty_word.liberty_id == liberty.id,
                                                     Liberty_word.word_id == word.id).first()
    session.delete(liberty_word)
    session.commit()
    session.close()


def get_nikname(user_id: int):
    session = session_factory()
    user = session.query(User).where(User.id == user_id).first()
    session.close()
    return user.nickname


def get_mail(user_id: int):
    session = session_factory()
    user = session.query(User).where(User.id == user_id).first()
    session.close()
    return user.mail


def get_phone(user_id: int):
    session = session_factory()
    user = session.query(User).where(User.id == user_id).first()
    session.close()
    return user.phone


def get_password(user_id: int):
    session = session_factory()
    user = session.query(User).where(User.id == user_id).first()
    session.close()
    return user.password


def update_user_nikname(user_id: int, new_nikname: str):
    session = session_factory()
    user = session.query(User).where(User.id == user_id).first()
    user.nickname = new_nikname
    session.commit()
    session.close()


def update_password(user_id: int, new_password: str):
    session = session_factory()
    user = session.query(User).where(User.id == user_id).first()
    user.password = new_password
    session.commit()
    session.close()


def check_phone(phone: str):
    session = session_factory()
    user = session.query(User).where(User.phone == phone).first()
    if user:
        return False
    else:
        return True


def update_phone(user_id: int, new_phone: str):
    session = session_factory()
    user = session.query(User).where(User.id == user_id).first()
    user.phone = new_phone
    session.commit()
    session.close()


def check_mail(mail: str):
    session = session_factory()
    user = session.query(User).where(User.mail == mail).first()
    if user:
        return False
    else:
        return True


def update_mail(user_id: int, new_mail: str):
    session = session_factory()
    user = session.query(User).where(User.id == user_id).first()
    user.mail = new_mail
    session.commit()
    session.close()


def get_not_studied_words(user_id):
    session = session_factory()
    liberty = session.query(Liberty).where(Liberty.user_id == user_id).first()
    liberty_words = session.query(Liberty_word).where(Liberty_word.liberty_id == liberty.id,
                                                      Liberty_word.true_or_false == False).all()
    words = []
    if liberty_words:
        for i in liberty_words:
            words.append(session.query(Word).where(Word.id == i.word_id).first())
    session.close()
    return words


def get_studied_words(user_id):
    session = session_factory()
    liberty = session.query(Liberty).where(Liberty.user_id == user_id).first()
    liberty_words = session.query(Liberty_word).where(Liberty_word.liberty_id == liberty.id,
                                                      Liberty_word.true_or_false == True).all()
    words = []
    if liberty_words:
        for i in liberty_words:
            words.append(session.query(Word).where(Word.id == i.word_id).first())
    session.close()
    return words