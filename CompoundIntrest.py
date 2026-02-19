p = int(input("Enter P: "))
t = int(input("Enter T: "))
r = int(input("Enter R: "))
n = int(input("Enter N: "))

res = p * (1 + (r / n)) ** (n ** t)
print(res)
