list_int = [i for i in range(20)]

my_iterator = iter(list_int)

# print(next(my_iterator))
# print(next(my_iterator))

# for elemento in my_iterator:
#     print(elemento)

while True:
    try:
        elemento = next(my_iterator)
        print(elemento)
    except StopIteration:
        break



class MeuIterator:
    def __init__(self, max=0):
        self.__max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.__max:
            resultado = 2 ** self.n
            self.n += 1
            return resultado
        else:
            raise StopIteration



for i in MeuIterator(5):
    print(i)