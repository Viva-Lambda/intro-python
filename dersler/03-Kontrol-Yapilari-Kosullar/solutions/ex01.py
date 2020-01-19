"""
Solution to Exercice 01
"""
# Author: Kaan Eraslan
# License: see, LICENSE


if __name__ == "__main__":
    text = """
    Gördün mü hiç suyun yanmasını tuzda
    Gördüm ben bu yaşam boyu iniltiyi
    Büyük bahçelerin küçük içinde
    Saksılardan birinde
    Gördüm de
    Uyurken uyandırılmış gibi
    Beni bir sardunya büyüttü belki.

    O ben ki
    Bir kadında bir çocuk hayaleti mi
    Bir çocukta bir kadın hayaleti mi
    Yalnızca bir hayalet mi yoksa.
    """
    saisi = input("Metin giriniz: ")
    if saisi in text:
        print("Girdiginiz metin: " + saisi + " metinde geçiyor")
    else:
        print("Girdiginiz metin metinde geçmiyor")
