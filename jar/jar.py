
class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        if int(capacity) < 0:
            raise ValueError('Capacity cannot be negative')
        print(f'Capacity is {self.capacity}')


    def __str__(self):
        return f'{self.capacity}'


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


    # @capacity.setter
    # def capacity(self, capacity):
    #     self._capacity = capacity


    @classmethod
    def get(cls):
        add = input('Add cockie: ')
        eat = input('Eat cockie: ')
        return cls(add, eat)


def main():
    jar = Jar.get()
    print(jar)


if __name__ == "__main__":
    main()
