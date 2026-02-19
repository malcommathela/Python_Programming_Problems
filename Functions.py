def hello(name,surname,age):
    print("Hello! "+name +surname)
    print("You are "+str(age)+" years old")
    print("Have a nice day")


def sum_of_all(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(result)


# name = "Dude
hello("Bro","Code",21)
sum_of_all(1,2,3,4,5)