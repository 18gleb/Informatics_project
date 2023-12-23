from pickle import dump

from CRUD import create_Word


def add_word_in_database(on_rus: str, on_eng: str, way_before_mp3: str):
    with open(way_before_mp3, "rb") as input, open("working.txt", "wb") as output:
        st = input.read()
        dump(st, output)
    with open("working.txt", "rb") as input:
        create_Word(on_rus, on_eng, input.read(), 1)


add_word_in_database("молоко", "milk", r"C:\Users\1\Desktop\озвучка\p_26305143_967.mp3")
add_word_in_database("мясо", "meat", r"C:\Users\1\Desktop\озвучка\p_26309403_270.mp3")
add_word_in_database("хлеб", "bread", r"C:\Users\1\Desktop\озвучка\p_26309436_346.mp3")
add_word_in_database("масло", "butter", r"C:\Users\1\Desktop\озвучка\p_26309460_442.mp3")
add_word_in_database("чеснок", "garlic", r"C:\Users\1\Desktop\озвучка\p_26309582_544.mp3")
add_word_in_database("лук", "onion", r"C:\Users\1\Desktop\озвучка\p_26309610_588.mp3")
add_word_in_database("рыба", "fish", r"C:\Users\1\Desktop\озвучка\p_26309643_667.mp3")
add_word_in_database("рис", "rice", r"C:\Users\1\Desktop\озвучка\p_26309683_789.mp3")
add_word_in_database("добрый", "kind", r"C:\Users\1\Desktop\озвучка\p_26309854_23.mp3")
add_word_in_database("храбрый", "brave", r"C:\Users\1\Desktop\озвучка\p_26309922_151.mp3")
add_word_in_database("скучный", "boring", r"C:\Users\1\Desktop\озвучка\p_26309948_242.mp3")
add_word_in_database("велосипед", "bicycle", r"C:\Users\1\Desktop\озвучка\p_26310032_446.mp3")
add_word_in_database("машина", "car", r"C:\Users\1\Desktop\озвучка\p_26310041_524.mp3")
add_word_in_database("вертолёт", "helicopter", r"C:\Users\1\Desktop\озвучка\p_26310086_675.mp3")
add_word_in_database("лев", "lion", r"C:\Users\1\Desktop\озвучка\p_26310114_764.mp3")
add_word_in_database("волк", "wolf", r"C:\Users\1\Desktop\озвучка\p_26310131_828.mp3")
add_word_in_database("собака", "dog", r"C:\Users\1\Desktop\озвучка\p_26310172_919.mp3")
add_word_in_database("лягушка", "frog", r"C:\Users\1\Desktop\озвучка\p_26310311_6.mp3")
add_word_in_database("ручка", "pen", r"C:\Users\1\Desktop\озвучка\p_26310345_82.mp3")
add_word_in_database("карандаш", "pencil", r"C:\Users\1\Desktop\озвучка\p_26310370_144.mp3")
add_word_in_database("резинка", "rubber", r"C:\Users\1\Desktop\озвучка\p_26310408_245.mp3")
add_word_in_database("линейка", "ruler", r"C:\Users\1\Desktop\озвучка\p_26310441_328.mp3")
add_word_in_database("циркуль", "compass", r"C:\Users\1\Desktop\озвучка\p_26310512_420.mp3")
add_word_in_database("стол", "table", r"C:\Users\1\Desktop\озвучка\p_26310557_582.mp3")
add_word_in_database("стул", "chair", r"C:\Users\1\Desktop\озвучка\p_26310604_657.mp3")

















