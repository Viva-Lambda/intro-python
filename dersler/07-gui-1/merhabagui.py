# author: Qm Auber
# license: see, LICENSE
###############################
# LISANSIN ANA METNI
###############################

import tkinter as tk


class MerhabaPenceresi:
    def __init__(self, master):
        self.cerceve = tk.Frame(master)
        self.cerceve.pack()

        # etiket
        self.etiket_yazisi = tk.StringVar()
        self.etiket = tk.Label(self.cerceve, textvariable=self.etiket_yazisi)
        self.etiket.pack(side=tk.TOP, expand=1, fill=tk.X)

        # merhaba dugmesi
        self.mdugme = tk.Button(self.cerceve, text="Merhaba", command=self.merhaba_de)
        self.mdugme.pack(side=tk.LEFT, expand=1, fill=tk.X)

        # ne haber dugmesi
        self.ndugme = tk.Button(self.cerceve, text="Ne haber", command=self.nehaber_de)
        self.ndugme.pack(side=tk.LEFT, expand=1, fill=tk.X)

        # cikis dugmesi
        self.cdugme = tk.Button(self.cerceve, text="Çıkış", command=self.cerceve.quit)
        self.cdugme.pack(side=tk.LEFT, expand=1, fill=tk.X)

    def merhaba_de(self):  # self.merhaba_de()
        "etiket yazisini merhabaya degistir"
        self.etiket_yazisi.set("Merhaba kardeş")
        return None

    def nehaber_de(self):
        "etiket yazısını ne habere degistir"
        self.etiket_yazisi.set("Ne haber kardeş, nasıl gidiyor ?")
        return None


if __name__ == "__main__":
    tutucu = tk.Tk()
    pencere = MerhabaPenceresi(tutucu)
    tutucu.mainloop()
