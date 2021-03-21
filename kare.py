#!/usr/bin/env python
# -*- coding: utf-8 -*-
#for i in range(0,11):
#    if i % 2 == 0:
#        print(pow(i, 2))


while True:
    sayi = raw_input("lütfen karesini almak istediğiniz sayıyı giriniz: " )
    if sayi == "iptal":
        break
    else:
        print(pow(int(sayi), 2))
