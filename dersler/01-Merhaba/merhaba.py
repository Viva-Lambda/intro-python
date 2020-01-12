"""
Iki ondalik sayi arguman alir. Bir islem tipi argumani alir.
Onlardan belirtilen islemi gerçeklestirir. Ornegin
arguman 1 = 2.6
arguman 2 = 3.5
arguman 3 = +

cikti 3.5 + 2.6
"""


def hesapla(sayi1: float, sayi2: float, operator: str) -> float:
    "sayi1 ve sayi2 ile operatorde verilen islemi gerçeklestir"
    "+-*/"
    gecerli_operator = ["+", "-", "*", "/"]
    gecerlidir = False
    for gop in gecerli_operator:
        if gop == operator:
            gecerlidir = True
    #
    if gecerlidir == False:
        raise ValueError("YANLIS OPERATOR: " + operator + "." + str(gecerli_operator))
    if operator == "+":
        return sayi1 + sayi2
    elif operator == "-":
        return sayi1 - sayi2
    elif operator == "*":
        return sayi1 * sayi2
    else:
        return sayi1 / sayi2


if __name__ == "__main__":
    s1 = input("Birinci sayiyi giriniz: ")
    s2 = input("Ikinci sayiyi giriniz: ")
    ops = input("Operatoru giriniz [+,-,*,/]: ")
    s1f = float(s1)
    s2f = float(s2)
    sonuc = hesapla(sayi1=s1f, sayi2=s2f, operator=ops)
    # hesapla(s1, s2, ops)
    print("Isleminizin sonucu:", str(sonuc))
