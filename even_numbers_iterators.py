class EvenNumbers:
    def __init__(self, number=None):
        if number == None:
            self.number = 0
        else:
            self.number = number

    def __iter__(self):
        self.a = 2
        return self

    def __next__(self):
        if self.a <= self.number:
            x = self.a
            self.a += 2
            return x
        raise StopIteration
        
num = EvenNumbers(9)
my_iter = iter(num)

print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
