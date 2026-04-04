grades = []
for j in range(10):
    grades.append(int(input("Enter grades: ")))
grademax = 0
grademin = 1000
gradesum = 0
gradefails = 0
for i in grades:
    gradesum += i
    if grademax < i:
        grademax = i
    if grademin > i:
        grademin = i
    if i < 60:
        gradefails += 1
gradeaverage = gradesum / len(grades)

print("The average grade is ", int(gradeaverage))
print("The maximum grade is ", grademax)
print("The minimum grade is ", grademin)
print("The grade sum is ", gradesum)
print("The number of the grade fails is ", gradefails)