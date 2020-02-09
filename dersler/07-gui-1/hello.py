# author: Qm.Auber
# license: see, LICENSE

import tkinter as tk


class MerhabaPenceresi:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()
        #
        self.labeltxt = tk.StringVar()
        self.label = tk.Label(self.frame, textvariable=self.labeltxt)
        self.label.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

        # merhaba butonu
        self.mbtn = tk.Button(self.frame, text="Merhaba", command=self.merhaba_de)
        self.mbtn.pack(side=tk.LEFT, expand=1, fill=tk.X)

        # ne haber butonu
        self.nbtn = tk.Button(self.frame, text="Ne haber", command=self.nehaber_de)
        self.nbtn.pack(side=tk.LEFT, expand=1, fill=tk.X)

        # çikis butonu
        self.cbtn = tk.Button(self.frame, text="Çıkış", command=self.frame.quit)
        self.cbtn.pack(side=tk.LEFT, expand=1, fill=tk.X)

    def merhaba_de(self):
        self.labeltxt.set("Merhaba kardeş")

    def nehaber_de(self):
        self.labeltxt.set("Ne haber kardeş, nasıl gidiyor?")


if __name__ == "__main__":
    ana = tk.Tk()
    app = MerhabaPenceresi(ana)
    ana.mainloop()
