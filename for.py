while True:
    parola = input("bir parola belirleyin")

    if not parola:
        print("parola boş bırakılamaz")
    elif len(parola) in range(3,8):
        print("yeni parolanız:", parola)
        break
    else:
        print("paroalnız 8 karakterden uzun 3 karakterden kısa olamaz")
        break
