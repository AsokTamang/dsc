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




#Optimizing API Usage with Caching for Client Financial Data Retrieval
def cache_decorator(func):
    storage = {}

    def wrapper(*args):
        if args[0] in storage:  # if the ticker has already been called then we return from our storage
            print(f'{args[0]} is in storage, no need for api call')
            return storage[args[0]]
            # if the ticker is not in our storage then we need to make an api call
        result = func(*args)
        storage[args[0]] = result
        print(f'{args[0]} wasnot in storage,need for api call')
        return result

    return wrapper


@cache_decorator
def get_company_name(ticker):
    # here we are making an api call
    api_responses = {
        "AAPL": "Apple Inc.",
        "MSFT": "Microsoft Corporation",
        "GOOGL": "Alphabet Inc."}
    return api_responses.get(ticker)


# Test the decorated function
print(get_company_name("AAPL"))  # Expected to trigger an API call
print(get_company_name("AAPL"))  # Expected to use cached data
print(get_company_name("MSFT"))  # Expected to trigger an API call
print(get_company_name("MSFT"))  # Expected to use cached data
print(get_company_name("GOOGL"))  # Expected to trigger an API call
print(get_company_name("GOOGL"))  # Expected to use cached data