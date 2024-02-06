from collections.abc import Iterable
class Employee:
    def __init__(self, first, last):
        self._first = first
        self._last = last
        

    @property
    def Name(self):
        return self._first + " " + self._last

def main():

    name = Employee("Spongebob", "Squarepants")
    print("Employee at the Krusty Krab:", name.Name)

    name2 = Employee("squidward", "Tentacles")
    print("Employee at the Krusty Krab:", name2.Name)

if __name__ == "__main__":
    main()