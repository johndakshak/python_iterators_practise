class Countdwon:
    def __init__(self, number):
        self.number = number
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number >= 0:
            x = self.number
            self.number -= 1
            return x
        else:
            raise StopIteration
    
count = Countdwon(5)
my_iter = iter(count)

print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))