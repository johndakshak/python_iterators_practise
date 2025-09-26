class MyRange:
    def __init__(self, start, stop=None):
        if stop == None:
            self.start = 0
            self.stop = start
        
        else:
            self.start = start
            self.stop = stop

    def __iter__(self):
        self.a = self.start
        return self
    
    def __next__(self):
        if self.start < self.stop:
            x = self.start
            self.start += 1
            return x
        
        else:
            raise StopIteration
            
range = MyRange(5)
my_iter = iter(range)

print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))