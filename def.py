#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dilekce_gonder(isim, tarih, gonderen):
    print """\
     Sayın %s,
     %s tarihinde yaptığımız başvurunun sonuçlandırılması
     hususunda yardımlarınızı rica ederiz.
     Saygılarımızla,
     %s """  %(isim,tarih,gonderen)


dilekce_gonder(raw_input("alıcı adını giriniz"),raw_input("tarih griniz"),raw_input("gönderen adı giriniz"))