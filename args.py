# args = parameter that will pack all arguments into a turple
#        useful so that a functions can accept a varying amount of arguments


# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
# print(add(1,2,3))

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))