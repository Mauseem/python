# -*- coding: utf-8 -*-
import os
def dizinler(test1, test2, test3):
    os.makedirs(test1)
    os.makedirs(os.sep.join([test1, test2]))
    os.makedirs(os.sep.join([test1, test3]))
