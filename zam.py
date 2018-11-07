# -*- coding: utf-8 -*-
def terfi_ettir(kisi, e_poz, y_poz, e_maas, z_orani):
     print "%s, %s pozisyonundan %s pozisyonuna terfi etmiştir!" \
     %(kisi,
e_poz,
       y_poz)
     print "Bu kişinin %s TL olan maaşı %s TL'ye yükseltilmiştir!" \
     %(e_maas,
       e_maas +
       (e_maas * z_orani / 100))
terfi_ettir(e_maas = 3500,
            e_poz = "İş Geliştirme Uzmanı",
            kisi = "Ahmet Öncel",
            y_poz = "İş Geliştirme Müdürü",
            z_orani = 25)