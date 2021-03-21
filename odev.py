#!/usr/bin/env python
# -*- coding: utf-8 -*-
def tek():
    print "Girdiğiniz sayı bir tek sayıdır!"
def cift():
    print "Girdiğiniz sayı bir çift sayıdır!"
sayi = input("Lütfen bir sayı giriniz: ")
if int(sayi) % 2 == 0:
       cift()
else: tek()