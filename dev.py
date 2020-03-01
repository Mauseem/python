# # # started = False
# # # while True:
# # #     command = input('> ').lower()
# # #
# # #     if command == 'help':
# # #        print('''
# # # start - to start the car
# # # stop - to stop the car
# # # quit - to exit''')
# # #     elif command == 'start':
# # #         if started :
# # #             print('car already started')
# # #         else:
# # #             started = True
# # #             print('car started')
# # #
# # #     elif command == 'stop':
# # #         if not started:
# # #             print('car already stopped')
# # #         else:
# # #             started = False
# # #             print('car stopped')
# # #     elif command == 'quit':
# # #         print('Program terminated')
# # #         break
# # #     else:
# # #         print(' I dont understand that')
# #
# # for item in 'pytHOn'.upper():
# #     print(item)
#
# # prices = [10,20,30]
# #
# # total = 0
# # for item in prices:
# #     total += item
# # print(f'Total:  {total}')
#
#
# # numbers = [5,2,5,2,2]
# # for x_count in numbers:
# #     for y in str(x_count):
# #         print(int(y) * 'X')
# #
# # numbers = [5,2,5,2,2]
# # for x_count in numbers:
# #     output = ''
# #     for count in range(x_count):
# #         output +=  'X'
# #     print(output)
# #
# # numbers = [0,3,5,7,88,44]
# #
# # max = numbers[0]
# # for item in numbers:
# #     if item > max:
# #         max = item
# # print(max)
# #
# # numbers = [1,1,2,2,3,4,5,6]
# #
# # #remove number numbers.remove(item)
# # # for x in numbers:
# # #     occurence = numbers.count(x)
# # #     if occurence > 1:
# # #         numbers.remove(x)
# # # print(numbers)
# # uniques = []
# # for number in numbers:
# #     if number not in uniques:
# #         uniques.append(number)
# # print(uniques)
#
# numbers = {"1": "One",
#            "2": "Two",
#             "3": "Three",
#             "4": "Four",
#              "5": "Five"}
#
# code = input('Phone:')
# output = ""
# for item in code:
#     output += numbers.get(item, '!') + '   '
# print(output)

# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')
#
# greet_user(last_name='Ak', first_name='Abdulkerim')

# def square(number):
#     number * number
#
# print(square(32))


# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😀",
#         ":(": "😞"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# print(emoji_converter('Selam kerem umarim bugun guzel olur :) '))

### TRY Catch

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(risk)
except ZeroDivisionError:
    print('Age must be grater than 0')
except ValueError:
    print('Invalid value')





















