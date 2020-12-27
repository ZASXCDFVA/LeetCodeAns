import threading
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.condition = threading.Condition()
        self.status = 0

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.condition.acquire()

            while self.status != 0:
                self.condition.wait()

            printFoo()

            self.status = 1

            self.condition.notify()

            self.condition.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.condition.acquire()

            while self.status != 1:
                self.condition.wait()

            printBar()

            self.status = 0

            self.condition.notify()

            self.condition.release()


if __name__ == '__main__':
    foo = FooBar(10)

    t1 = threading.Thread(target=lambda: foo.foo(lambda: print("foo")))
    t2 = threading.Thread(target=lambda: foo.bar(lambda: print("bar")))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
