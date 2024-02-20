
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

