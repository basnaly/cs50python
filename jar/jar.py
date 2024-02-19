
class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        if capacity < 0:
            raise ValueError('Capacity cannot be negative')

    def __str__(self):
        return f'{self.capacity}'


    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size



