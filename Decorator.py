def logger(func):
    def wrapper():
        print("Function execution started")
        func()
        print("Function execution completed")
    return wrapper

@logger
def display():
    print("Welcome to Advanced Python")

display()