#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a = ["elma", "armut", "portakal"]
# for i in a:
#     print i.capitalize()
# b = "enflasyon"
# print b.upper()
# c = "DUMBUK"
# print c.lower()
# d = "AsFDdfgDFHDFşlhfmdfbdfFD"
# print d.swapcase()
#
# f = " bu işin yonu yok kardeşş"
# print f.title()
#
# print "f".center(10)
#
#
# for i in a:
#     if i.startswith("e"):
#         print i.replace("e", "z")


name = raw_input("lütfen isminizi giriniz")
if name.isspace():
    print"lütfen boş geçmeyiniz"
    name = raw_input("lütfen isminizi griniz")
    if name.isspace():
        print   "isim olarak boş geçemezsiniz, programdan çıkılıyor"
        exit(0)
elif not name.isspace() and name.startswith("a") and name.endswith("m"):
    print name.capitalize()
else:
    print "isminiz tespit edilemedi"

cevap = raw_input("isminizin büyük harfle yazılmasını isterseniz lütfen E tuşuna basınız  "  )
if cevap == "E":
    print name.upper()
else:
    print name.lower()
