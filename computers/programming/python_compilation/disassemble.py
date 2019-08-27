import dis
from pprint import pprint


def count_up_and_wait():
    print("Hello World")
    for i in range(100):
        input()
        print(i)


d = {}
dd = dict()

# print(dis.dis(count_up_and_wait))

print(dis.dis("{}"))
print(dis.dis("dict()"))
