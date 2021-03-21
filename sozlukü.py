#!/usr/bin/env python
# -*- coding: utf-8 -*-


def kayit_ekle(isim, soyisim, sehir, meslek, tel, adres):
    kayit = {}
    kayit["%s %s" % (isim, soyisim)] = [sehir, meslek, tel, adres]
    print "Bağlantı bilgileri kayıtlara eklendi!\n"
    for k, v in kayit.items():
        print k
        print "-" * len(k)
        for i in v:
            print i


kayit_ekle("Orçun", "Kunek", "Adana", "Şarkıcı", "0322 123 45 67", "Baraj Yolu")