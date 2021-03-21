def find_max(numbers):
    maks = numbers[0]
    for number in numbers:
        if number > maks:
            maks = number
    return maks
