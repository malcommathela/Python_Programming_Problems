
# squares = []
# for i in range(i,11):
#     squares.append(i * i)
# print(squares)

squares = [i * i for i in range(1,11)]


students = [100,90,80,70,60,50,40,30,0]

passed_students = list(filter(lambda x:x >= 60,students))

# passed_students = [i for i in students if i >= 60]
#
# passed_students = [i if i >= 60 else "Failed" for i in students]

print(passed_students)