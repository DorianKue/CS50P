class Jar:
    def __init__(self, capacity=12):
        # Initializing Jar with a capacity of 12 and size set to 0.
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        # Returning a string of cookie emojis based on the current size of the jar.
        return "🍪" * self.size

    def deposit(self, n):
        # Method to deposit cookies into the jar, which checks if adding n cookies would exceed the capacity and raises an error if it does.
        if self.size + n > self.capacity:
            raise ValueError
        # Adding the n cookies to the size if no error was raised.
        self.size += n

    def withdraw(self, n):
        # Method to withdraw cookies from the jar, which checks if you're withdrawing more cookies than available. If that's the case, raise an error.
        if n > self.size:
            raise ValueError
        # If no error was raised, withdrawing n cookies from the size.
        self.size -= n

    @property
    def capacity(self):
        # Getter for the capacity of the jar, which returns the capacity.
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        # Setter for the capacity of the jar, which checks if the capacity is < 1 and raises an error if that's the case.
        if capacity < 1:
            raise ValueError
        # If no error was raised, set the capacity of the jar.
        self._capacity = capacity

    @property
    def size(self):
        # Getter for the size of the jar, which returns the size.
        return self._size

    @size.setter
    def size(self, size):
        # Setter for the size of the jar, which checks if the size exceeds the capacity and raises an error if that's the case.
        if size > self.capacity:
            raise ValueError
        # If no error was raised, set the size of the jar.
        self._size = size
