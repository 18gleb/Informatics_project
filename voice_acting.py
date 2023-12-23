from playsound import playsound
from pickle import dump

from CRUD import get_by_field_word


def voice_acting(word_id):
    word = get_by_field_word(word_id)
    with open("word.mp3", "wb") as output:
        dump(word.how_to_listen, output)
    playsound("word.mp3")


voice_acting(30)
