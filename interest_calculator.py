def birikim_hesapla():
    bkumulatif = 0
    aylik_gelir = int(input('aylik toplm gelirinizi girini ormegin 120000   > '))
    anapara = aylik_gelir * 12
    zamorani = float(input('lutfen zam oraninini giriniz ornegin 0.18  >   '))
    zaman = int(input('lutfen hesaplama suresini belirtiniz, ornegin  dort yil icin  4 girebilirsiniz >   '))
    for x in range(1, zaman+1, 1):
        yillikzam = anapara * zamorani
        #zamlimaas = anapara + yillikzam
        print(f' yillik toplam gelir {anapara} lira')
        anapara += yillikzam
        bkumulatif += anapara
    print(f' %s yillik toplam   gelir {bkumulatif}  lirasidir' % zaman)
    secim()

def faiz_hesapla():
    fkumulatif = 0
    aylik_kira = int(input('lutfen kira tutarini giriniz  ornegin 1350  >   '))
    zaman = int(input('lutfen zaman araligi giriniz  ornegin 6 yil icin 6 yada 1  yil icin 1 girebilirsiniz >  '))
    zamorani = float(input('lutfen zam oraninini giriniz ornegin 0.18  >   '))
    for x in range(1, zaman+1):
        yillikzam = aylik_kira * zamorani
        # zamlimaas = anapara + yillikzam
        print(f'1 yillik kira toplami =  { round(aylik_kira * 12)} lira')
        fkumulatif += aylik_kira * 12
        aylik_kira += yillikzam
        print(f'bu yil yapilan zam  {round(yillikzam)} lira')
        print(f'yeni kira {round(aylik_kira)} lira  {x+1}.yil')
    print(f'Toplam Odenen Kira = {zaman}  yil icin {fkumulatif} lira')
    secim()

def secim():
    response = int(input('Birikimlerinizi mi yoksa, kira giderinizi mi hesaplamak istersiniz ? birikim icin 1 kira icin 2 tusuna basiniz, cikmak icin 3 tusuna basiniz     '))
    if response == 1:
        birikim_hesapla()
    elif response == 2:
        faiz_hesapla()
    elif response == 3:
        exit()
    else:
        print('lutfen 1 yada 2 seciniz, cikmak icin 3 seciniz')

secim()


