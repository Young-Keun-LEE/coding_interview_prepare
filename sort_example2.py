N = int(input())
student_info = []
info = []
for i in range(N):
    info = input().split()
    student_info.append((info[0],info[1]))
     
student_info.sort(key = lambda student: student[1])

for student in student_info:
    print(student[0])