#!/usr/bin/env python
# -*- coding: utf-8 -*-
sifreli_metin = """saüipö 1990 ajnjöfcö çv acöc çyaym çkş
üpsnvnvm ücşcğjöfcö hgnkuükşkngö mjzşcm zg fköcokm çkş fknfkş.
trb fkbkokökö tcfg pnoctj, mpnca rışgöknogtk zg sşphşco
hgnkuükşog tyşgdkök ijbncöfjşoctj kng ücöjöcö çv fkn
wköfpwt, höv/nkövx zg ocdpt x hkçk sgm epm ğcşmnj kungüko
tktügok ybgşköfg ecnjucçknogmügfkş. fpncajtjanc ügm çkş
sncüğpşofc hgnkuükşfkıkökb çkş saüipö vahvncoctj, ybgşköfg
ike çkş fgıkukmnkm acsocac hgşgm pnocfcö zgac myeym
fgıkukmnkmngşng çcumc sncüğpşoncşfc fc ecnjucçkngdgmükş."""
sozluk = {"a": "y", "b": "z", "c": "a",
          "ç": "b", "d": "c", "e": "ç",
          "f": "d", "g": "e", "ğ": "f",
          "h": "g", "ı": "ğ", "i": "h",
          "j": "ı", "k": "i", "l": "j",
          "m": "k", "n": "l", "o": "m",
          "ö": "n", "p": "o", "r": "ö",
          "s": "p", "ş": "r", "t": "s",
          "u": "ş", "ü": "t", "v": "u",
          "y": "ü", "z": "v"}
sifresiz_metin = ""
for harf in sifreli_metin:
    sifresiz_metin += sozluk.get(harf, harf)
print sifresiz_metin