import time
def timer(func):  #this is our decorator function
    def wrapper(*args, **kwargs):  #which has an inner function called wrapper
        start = time.time()
        result  = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} function took {(end-start) * 1000} milli-seconds')
        return result
    return wrapper
@timer   #using timer function as decorator
def find_multiplication(num):
    return num ** (num -1)
print(find_multiplication(100000))