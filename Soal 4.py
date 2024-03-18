# Nama: Hanzel Oclihar Tjiam
# NIM: 221402064

# Soal 4
grades = []

while True:
    x = int(input("Enter a grade: "))
    if x == -1 :
        break
    grades.append(x)

if len(grades) > 0:
    print(int(sum(grades) / len(grades)))
    for i in range(len(grades)):
        print(grades[i])
else:
    print("The list grades is empty!")
