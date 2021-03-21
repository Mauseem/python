import time
def calculate_time(func):
    def wrapper(numbers):
        start = time.time()
        result = func(numbers)
        end = time.time()
        print(func.__name__ + "  " + str(end-start) + " saniye sürdü.")
        return result
    return wrapper

@calculate_time
def kareleri_hesapla(numbers):
    result = list()
    for i in numbers:
        result.append(i ** 2)
        return result

kareleri_hesapla(range(1000))