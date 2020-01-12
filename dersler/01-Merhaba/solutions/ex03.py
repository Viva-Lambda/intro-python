"""
Solution de exercice 03
"""
# author: Kaan Eraslan
# license: see, LICENSE


if __name__ == "__main__":
    str1 = "bir kucuk"
    str2 = "ev"
    print(str2 + str1)
    print(str1 + str2)
    str1 = "bir {0} kucuk"
    print(str1.format(str2))
