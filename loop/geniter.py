class Controller:
    def __init__(self):
        self.data = [1,2,3]
        self.index = -1
    def __next__(self):  #the feature of next is to find the next value from the current iteration value
        self.index += 1
        if self.index >= len(self.data):   #if the index value becomes greater than the length of the data then we raise the exception
            raise StopIteration
        return self.data[self.index]
    def __iter__(self):
        return self
c=Controller()
for data in c:
    print(data)

#so the main advantage of using generator is that we can read or iterate over the objects from large volume of data without facing the slowness and memory full outburst with the help
#of yield which only returns the required data at the current iteration without closing the function, as the function stops temporarily and again resumes from the current state

#fibonacci series using generators
def gen_fib():
    a,b= 0,1
    while True:
        yield a
        a,b = b,a+b
fb=gen_fib()
for _ in range(10):
    print(next(fb))  #only by using next we can print the yieled value from the function otherwise we will only get the generator object

