from data_base import session_factory, User, Liberty, Word, Liberty_word


def create_User(mail, phone, password, nickname):
    session = session_factory()
    user = User(mail=mail, phone=phone, password=password, nickname=nickname)
    session.add(user)
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


def get_by_field_word(id):
    session = session_factory()
    word = session.query(Word).group_by(Word.id).all()
    session.close()
    return Word


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
    liberty_word = Liberty_word()
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
