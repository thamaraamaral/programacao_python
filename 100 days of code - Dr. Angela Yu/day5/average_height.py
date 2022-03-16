student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0

for height in student_heights:
    total = total + height

number_students = int(n+1)

average = round(total/number_students)

print(average)