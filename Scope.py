# Scope = The region that a variable is recognised
#         A variable is only available from inside the region it is created
#         A global nad locally scoped versions of a variable can be created

name = "Code"  # global scope (available only inside and outside  functions)
def display_name():
    name = "Bro"   # local scope (available only inside this function)
    print(name)

