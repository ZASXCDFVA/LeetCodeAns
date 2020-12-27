import threading
from typing import Callable, List


class ZeroEvenOdd:
    def __init__(self, n):
        def generate(_n):
            for i in range(_n):
                yield 0
                yield i + 1

        self.sequence: List[int] = list(generate(n))
        self.index: int = 0
        self.condition = threading.Condition()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        self.condition.acquire()

        while self.index < len(self.sequence):
            if self.sequence[self.index] == 0:
                printNumber(0)

                self.index += 1

                self.condition.notify_all()
            else:
                self.condition.wait()

        self.condition.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        self.condition.acquire()

        while self.index < len(self.sequence):
            current = self.sequence[self.index]

            if current != 0 and current % 2 == 0:
                printNumber(current)

                self.index += 1

                self.condition.notify_all()
            else:
                self.condition.wait()

        self.condition.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        self.condition.acquire()

        while self.index < len(self.sequence):
            current = self.sequence[self.index]

            if current != 0 and current % 2 == 1:
                printNumber(current)

                self.index += 1

                self.condition.notify_all()
            else:
                self.condition.wait()

        self.condition.release()


if __name__ == '__main__':
    obj = ZeroEvenOdd(10)

    t1 = threading.Thread(target=lambda: obj.zero(lambda x: print(x)))
    t2 = threading.Thread(target=lambda: obj.odd(lambda x: print(x)))
    t3 = threading.Thread(target=lambda: obj.even(lambda x: print(x)))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
