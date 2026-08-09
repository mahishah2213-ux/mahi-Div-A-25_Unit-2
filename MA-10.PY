m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

total = m1 + m2 + m3
print("Total =", total)

if total >= 90:
    print("Grade A+")
elif total >= 80:
    print("Grade A")
elif total >= 70:
    print("Grade A-")
elif total >= 60:
    print("Grade B+")
elif total >= 50:
    print("Grade B")
elif total >= 40:
    print("Grade C")
else:
    print("Fail")
