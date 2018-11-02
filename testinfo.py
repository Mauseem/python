#!/usr/bin/python
user_name = input("enter your user name")
password = input("enter your password")
count = len(user_name) + len(password)

message = "your info contains  {} characters !"

print(message.format(count))
if count > 40:
    print("please do not use more than 40 characters")
else:
    print("welcome")