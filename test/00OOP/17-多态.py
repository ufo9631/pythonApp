class Dog():
    def print_self(self):
        print("hello world .....")

class Xiaotq(Dog):
    def print_self(self):
        print("hello everybody,我是大佬")


def introduce(temp):
    temp.print_self()

dog1=Dog()
dog2=Xiaotq()

introduce(dog1)
introduce(dog2)
