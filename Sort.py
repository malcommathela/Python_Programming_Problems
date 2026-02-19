#--------------Level 1-------------#

# students = ["Blahhh","hewde","gdsjeu","hdjsd","hdsjd"]

# students.sort(reverse=True)
#
# for i in students:
#     print(i)

#---------------also level 1-------------------#

# sorted_students = sorted(students)
#  for i in sorted_students:
#     print(i)


#-------------level2-------------------#

students = [("hbwejhwnwj","E",60),
            ("benkercele","A",33),
            ("ldjeybjd","D",35),
            ("vdfeskdeip","B",20),
            ("agsudmdjek","C",78)]


# grade = lambda grades:grades[1]
age = lambda age:age[2]
#
#
# students.sort(key=grade,reverse=True)
# for i in students:
#     print(i)
#
# students.sort(key=age,reverse=True)
# for i in students:
#     print(i)

sorted_students = sorted(students,key=age)
for i in sorted_students:
    print(i)