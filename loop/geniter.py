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

#so the main advantage of using generator is that we can read or unpack the objects from large volume of data without facing the slowness and memory full outburst with the help
#of yield which only returns the required data at the current iteration without stopping the function

