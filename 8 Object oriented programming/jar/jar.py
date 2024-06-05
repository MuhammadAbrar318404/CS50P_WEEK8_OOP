import sys

class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Exceeds jar capacity")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = None
    while True:
        print("\n1. DEFINE CAPACITY OF THE JAR OTHERWISE 12 IS DEFAULT\n2. DO YOU WANT TO DEPOSIT?\n3. DO YOU WANT TO WITHDRAW?\n4. SHOW COOKIES\n5. EXIT")
        choice = int(input("\nChoose an option: "))

        if choice == 1:
            capacity = int(input("ENTER THE CAPACITY: "))
            jar = Jar(capacity)
        elif choice == 2:
            if jar is None:
                print("Please define the capacity of the jar first.")
                continue
            dep = int(input("DEPOSIT: "))
            try:
                jar.deposit(dep)
                print("\n",jar)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 3:
            if jar is None:
                print("Please define the capacity of the jar first.")
                continue
            withdraw = int(input("WITHDRAW: "))
            try:
                jar.withdraw(withdraw)
                print("\n",jar)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 4:
            if jar is None:
                print("Please define the capacity of the jar first.")
            else:
                print("\n",jar)
        elif choice == 5:
            sys.exit()
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
