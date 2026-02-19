import functools

letter = ["H", 'E', 'L', 'L', 'O']
word = functools.reduce(lambda x, y,: x + y, letter)
print(word)

fuctorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y,:x * y,fuctorial)
print(result)
