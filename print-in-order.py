import threading
from typing import Callable


class Foo:
    def __init__(self):
        self.condition = threading.Condition()
        self.step = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.condition.acquire()

        while self.step != 0:
            self.condition.wait()

        printFirst()

        self.step += 1

        self.condition.notify_all()

        self.condition.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.condition.acquire()

        while self.step != 1:
            self.condition.wait()

        printSecond()

        self.step += 1

        self.condition.notify_all()

        self.condition.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.condition.acquire()

        while self.step != 2:
            self.condition.wait()

        printThird()

        self.step += 1

        self.condition.notify_all()

        self.condition.release()


if __name__ == '__main__':
    foo = Foo()

    t1 = threading.Thread(target=lambda: foo.first(lambda: print("A")))
    t2 = threading.Thread(target=lambda: foo.third(lambda: print("C")))
    t3 = threading.Thread(target=lambda: foo.second(lambda: print("B")))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
