# -*- coding: utf-8 -*-
import os
#os.makedirs("kerem1" + os.sep + "kerem4")
test1 = "Belgelerim"
test2 = "Hesaplamalar"
test3 = "Resimler"
os.makedirs(test1)
os.makedirs(os.sep.join([test1, test2]))
os.makedirs(os.sep.join([test1, test3]))