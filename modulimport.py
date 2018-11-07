#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sum import ortalama

liste = []

ilksayi = input("lütfen ilk sayıyı giriniz")
ikincisayi = input("ikinci sayiyi griniz")
ucuncusayi = input("üçüncü sayıyı giriniz")
liste.append(ilksayi)
liste.append(ikincisayi)
liste.append(ucuncusayi)

print(ortalama(liste))