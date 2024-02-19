
class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        if int(capacity) < 0:
            raise ValueError('Capacity cannot be negative')


    def __str__(self):
        return f'{self.capacity}'


    def deposit(self, n):
        capacity =  int(capacity) + n
        if capacity > 12:
            raise ValueError('Max capacity is 12')
        return capacity


    def withdraw(self, n):
        capacity = int(capacity) - n
        if capacity < 0:
            raise ValueError('Capacity cannot be negative')
        return capacity


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size


    # @capacity.setter
    # def capacity(self, capacity):
    #     self._capacity = capacity


    # @classmethod
    # def get(cls):
    #     add = input('Add cockie: ')
    #     eat = input('Eat cockie: ')
    #     return cls(add, eat)


def main():
    jar = Jar.get()
    print(jar)


if __name__ == "__main__":
    main()
