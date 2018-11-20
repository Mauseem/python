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

macera = Oyun()
macera.goster()

