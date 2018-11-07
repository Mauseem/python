#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isim():
    isim = raw_input("lütfen adınızı giriniz")
    if len(isim) > 5:
        print(isim[0:6] + "...")
    else:
        print(isim)
isim()