#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Oyun:
    def __init__(self):
        self.enerji = 50
        self.para = 100
        self.fabrika = 4
        self.isci = 10

    def goster(self):
        print "enerji:", self.enerji
        print "para:", self.para
        print  "fabrika:", self.fabrika
        print "işçi:",  self.isci

    def fabrikakur(self, miktar):
        if self.enerji > 3 and self.para > 10:
            self.fabrika  =miktar + self.fabrika
            self.enerji = self.enerji - 3
            self.para = self.para - 10
            print miktar, "adet fabrika kurdunuz Tebrikler"
        else:
            print   "yeni fabrika kuramazsınız. \ " \
                    "yeterli kaynağınız yok !"


class Dusman(Oyun):
    def __init__(self):
        Oyun.__init__(self)
        self.ego = 0
    def goster(self):
        Oyun.goster(self)
        print "ego:", self.ego


    def fabrikayik(self, miktar):
        macera.fabrika = macera.fabrika - miktar
        self.ego = self.ego + 2
        print "tebrikler. Oyuncunun ", miktar, \
        "adet fabrikasını yıktınız"
        print "üstelik egonuzda büyüdü"


dusman = Dusman()
macera = Oyun()
dusman.fabrikayik(2)
dusman.goster()

