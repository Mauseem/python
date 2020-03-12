def faiz_hesapla():
    kumulatif = 0
    anapara = 2350
    zamorani = 0.10
    for x in range(1, 10, 1):
        yillikzam = anapara * zamorani
        #zamlimaas = anapara + yillikzam
        anapara += yillikzam
        kumulatif += anapara
        print(anapara , "anapara" )
        print(kumulatif , "kumulatif")
faiz_hesapla()