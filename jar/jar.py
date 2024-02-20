
class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        if self.capacity < 0:
            raise ValueError('Capacity canot be less 0')
        self.size = 0


    def __str__(self):
        return '🍪' * self.size


    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError(f'Size cannot be more than capacity of{self.capacity}!')
        self.size = self.size + n


    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError('Size cannot be less than 0!')
        self.size = self.size - n


    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity


    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar = Jar()
    jar.deposit(5)
    print(jar)
    jar.withdraw(2)
    print(jar)


if __name__ == '__main__':
    main()



