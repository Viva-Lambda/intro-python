"""
Simple calculator that computes the result given
two numbers and an operator
"""
# license: see LICENSE


def hesapla(sayi1: str, sayi2: str, op: str) -> float:
    "sayi1 sayi2 sayilariyla op islemini gerceklestir"
    sayi1f = float(sayi1)  # "1.5" -> 1.5
    sayi2f = float(sayi2)  # "53.3" -> 53.3
    gecerli_oplar = ["+", "-", "*", "/"]
    gecerlidir = False
    for gop in gecerli_oplar:
        if gop == op:
            gecerlidir = True
    #
    if gecerlidir is False:
        raise ValueError(
            "Gecerli olmayan bir operator girdiniz: "
            + op
            + ".\nLutfen {0} operatorlerinden birini giriniz.".format(str(gecerli_oplar))
        )
    if op == "+":
        return sayi1f + sayi2f
    elif op == "-":
        return sayi1f - sayi2f
    elif op == "*":
        return sayi1f * sayi2f
    else:
        return sayi1f / sayi2f


if __name__ == "__main__":
    sayi1s = input("Birinci sayiyi giriniz: ")
    sayi2s = input("Ikinci sayiyi giriniz: ")
    opstr = input("Islem tipini giriniz [+,-,/,*]: ")
    sonuc = hesapla(sayi1=sayi1s, sayi2=sayi2s, op=opstr)
    print("Isleminizin sonucu:", str(sonuc))
    # fin d'exécution
