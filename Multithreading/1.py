from threading import Thread

class Hello(Thread):
    def run(self):
        for i in range(50):
            print("Hello thread")

class Hi(Thread):
    def run(self):
        for i in range(50):
            print("Hi thread ")

obj1 = Hello()
obj2 = Hi()

obj1.start()
obj2.start()

print("Main thread")
