#!/usr/bin/python3
kullanıcı_adi = input("kullanıcı adınızı giriniz: ")
parola = input("parolanız: ")

if kullanıcı_adi == "kerem":
	if parola == "12345678":
		print("welcome")
	else:
		print("yanlış kullanıcı adı veya şifre!")
else:
	print( "yanlış kullanıcı adı veya şifre!")