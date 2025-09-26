class SquaresIterator:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= self.number:
            x = self.a
            self.a += 1
            return x**2
        raise StopIteration

square = SquaresIterator(5)
my_iter = iter(square)

print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))
print(next(my_iter, "StopIteration"))