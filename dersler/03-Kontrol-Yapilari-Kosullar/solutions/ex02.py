"""
Solution to Exercice 02
"""
# License: see, LICENSE


if __name__ == "__main__":
    OGRENCILER = {
        "ogrenci15": 0,
        "ogrenci242": 12,
        "ogrenci3": 10,
        "ogrenci4135": 14,
        "ogrenci345": 19,
        "ogrenci61": 16,
        "ogrenci887": 8,
    }
    for ismi, notu in OGRENCILER.items():
        if 0 <= notu and notu <= 9:
            print(ismi, ": unvani: ", "geçmez")
        elif 10 <= notu and notu <= 13:
            print(ismi, ": unvani: ", "geçer")
        elif 14 <= notu and notu <= 15:
            print(ismi, ": unvani: ", "iyi")
        elif 16 <= notu and notu <= 18:
            print(ismi, ": unvani: ", "çok iyi")
        elif 19 <= notu and notu <= 20:
            print(ismi, ": unvani: ", "pek iyi")
