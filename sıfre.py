#!/usr/bin/env python
# -*- coding: utf-8 -*-
kullanici_adi = "kullanici"
parola = "parola"
while True:
     soru1 = raw_input("Kullanıcı adı: ")
     soru2 = raw_input("Parola: ")
     if soru1 == kullanici_adi and soru2 == parola:
        print "Kullanıcı adı ve parolanız onaylandı."
        break
     else:
        print "Kullanıcı adınız veya parolanız yanlış."
        print "Lütfen tekrar deneyiniz!"
