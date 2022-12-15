import math
print('задание 1')
students = []
student1 = ['Mark', 'man', 'otl']
students.append(student1)
student2 = ['Igor', 'man', 'tr']
students.append(student2)
student3 = ['Olga', 'woman', 'tr']
students.append(student3)
student4 = ['Maria', 'woman', 'hor']
students.append(student4)
for i in range(3):
    if students[i][1] == 'man' and (students[i][2] == 'otl' or students[i][2] == 'hor') :
        print(students[i][0])
print('задание 2')
x= int(input())
y = int(input())
print((math.sin(x)**2 + math.cos(y)**2)* 2)