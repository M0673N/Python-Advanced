n = int(input())
students = {}
for i in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for student, grades in students.items():
    print(f"{student} -> {' '.join(map(lambda x: f'{x:.2f}', students[student]))} "
          f"(avg: {sum(grades) / len(grades):.2f})")
