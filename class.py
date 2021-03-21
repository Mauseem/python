#!/usr/bin/env python
# -*- coding: utf-8 -*-

class araba:
    def __init__(self,renk):
        self.model = "leon"
        self.marka =  "seat"
        self.renk = renk



class insan:
    isim = None
    soyisim = None
    araba = araba("kırmızı")

    def __init__(self,isim):
        self.isim = isim
        self.soyisim = "ak"


insandegisken = insan("abdulkerim")



print insandegisken.araba.renk