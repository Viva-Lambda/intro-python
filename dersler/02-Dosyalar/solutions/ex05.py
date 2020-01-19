"""
Solution to Exercice 05
"""
# License: see, LICENSE

import os

if __name__ == "__main__":
    print("Salut ceux qui pensent avec des mots clés")
    delimit = input("Ayirici giriniz: ")
    mots = input("kelimeleri giriniz: ")
    if delimit not in mots:
        raise ValueError(
            "Ayirici karakter kullanilmamis: " + mots
        )
    #
    savepath = os.path.join("assets", "ex05-mes-mots-clés.txt")
    mots_separer = mots.split(delimit) # "merhaba,burasi,neresi" -> ["merhaba", "burasi", "neresi"]
    mots_espace = " ".join(mots_separer) # merhaba burasi neresi
    with open(savepath, "w", encoding="utf-8", newline="\n") as fd:
        fd.write("Dosya Basligi- Anahtar Kelimelerim")
        fd.write("\n")
        fd.write(mots)
        fd.write("\n")
        fd.write(mots_espace)
        fd.write("\n")
        fd.write(mots_separer.pop(0))
        for mot in mots_separer:
            fd.write("\n")
            fd.write(mot)
    print("Les mots sont enregistrés")
