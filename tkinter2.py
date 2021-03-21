#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
class Arayuz(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.pencerearaclari()

    def pencerearaclari(self):
        self.dugme = Button(self, text=raw_input("adınız nedir"), command=self.yaz)
        self.dugme.pack()

    def yaz(self):
        exit(0)

uygulama = Arayuz()
uygulama.mainloop()

