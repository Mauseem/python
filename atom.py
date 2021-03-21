#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

while True:
    secenek1 = "(1) toplama"
    secenek2 = "(2) çıkarma"

    print secenek1
    print secenek2


    soru = raw_input("Yapacağınız işlemi seçin: ")

    if soru == "1":
        sayi1 = input("toplama için ilk sayıyı girin")
        print sayi1
        sayi2 = input("toplama için ikinci sayıyı girin")
        sonuc = int(sayi1 + sayi2)
        print(sonuc * 20)
