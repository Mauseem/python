# # started = False
# # while True:
# #     command = input('> ').lower()
# #
# #     if command == 'help':
# #        print('''
# # start - to start the car
# # stop - to stop the car
# # quit - to exit''')
# #     elif command == 'start':
# #         if started :
# #             print('car already started')
# #         else:
# #             started = True
# #             print('car started')
# #
# #     elif command == 'stop':
# #         if not started:
# #             print('car already stopped')
# #         else:
# #             started = False
# #             print('car stopped')
# #     elif command == 'quit':
# #         print('Program terminated')
# #         break
# #     else:
# #         print(' I dont understand that')
#
# for item in 'pytHOn'.upper():
#     print(item)

# prices = [10,20,30]
#
# total = 0
# for item in prices:
#     total += item
# print(f'Total:  {total}')


# numbers = [5,2,5,2,2]
# for x_count in numbers:
#     for y in str(x_count):
#         print(int(y) * 'X')
#
# numbers = [5,2,5,2,2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output +=  'X'
#     print(output)

numbers = [0,3,5,7,88,44]

max = numbers[0]
for item in numbers:
    if item > max:
        max = item
print(max)