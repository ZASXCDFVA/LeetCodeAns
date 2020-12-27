import threading
from typing import Callable


class FizzBuzz:
    def __init__(self, n: int):
        self.sequence = [i + 1 for i in range(n)]
        self.condition = threading.Condition()
        self.index = 0

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        self.condition.acquire()

        while self.index < len(self.sequence):
            current = self.sequence[self.index]

            if current % 3 == 0 and current % 5 != 0:
                printFizz()

                self.index += 1
            else:
                self.condition.wait()

            self.condition.notify_all()

        self.condition.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        self.condition.acquire()

        while self.index < len(self.sequence):
            current = self.sequence[self.index]

            if current % 3 != 0 and current % 5 == 0:
                printBuzz()

                self.index += 1
            else:
                self.condition.wait()

            self.condition.notify_all()

        self.condition.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        self.condition.acquire()

        while self.index < len(self.sequence):
            current = self.sequence[self.index]

            if current % 3 == 0 and current % 5 == 0:
                printFizzBuzz()

                self.index += 1
            else:
                self.condition.wait()

            self.condition.notify_all()

        self.condition.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        self.condition.acquire()

        while self.index < len(self.sequence):
            current = self.sequence[self.index]

            if current % 3 != 0 and current % 5 != 0:
                printNumber(current)

                self.index += 1
            else:
                self.condition.wait()

            self.condition.notify_all()

        self.condition.release()


if __name__ == '__main__':
    obj = FizzBuzz(15)

    t1 = threading.Thread(target=lambda: obj.fizz(lambda: print("fizz")))
    t2 = threading.Thread(target=lambda: obj.buzz(lambda: print("buzz")))
    t3 = threading.Thread(target=lambda: obj.fizzbuzz(lambda: print("fizzbuzz")))
    t4 = threading.Thread(target=lambda: obj.number(lambda x: print(x)))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
