
class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        if int(capacity) < 0:
            raise ValueError('Capacity cannot be negative')
        print(f'Capacity is {self.capacity}')


    def __str__(self):
        return f'your Jar has {"🍪" * self.size} cookies while it\'s capacity is {self.capacity}'


    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError(f'Max capacity is {self.capacity}')
        self.size =  self.size + n


    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError(f'Cannot eat more than {self.size}')
        self.size = self.size - n


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, size):
        self._size = size


    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity


    @classmethod
    def get(cls, capacity):
        return cls(capacity)


def main():
    jar = Jar.get(12)
    print(jar)
    jar.deposit(3)
    print(jar)


if __name__ == "__main__":
    main()
