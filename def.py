#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dilekce_gonder(isim, tarih, gonderen):
    print("""\
     Sayın %s
     %s tarihinde yaptığımız başvurunun sonuçlandırılması
     hususunda yardımlarınızı rica ederiz.
     Saygılarımızla,
     %s """) % (isim, tarih, gonderen)


dilekce_gonder(input("alıcı adını giriniz"),input("tarih griniz"),input("gönderen adı giriniz"))