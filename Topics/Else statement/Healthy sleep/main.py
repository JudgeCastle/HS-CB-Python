A = int(input())
B = int(input())
H = int(input())

if H <= B and H >= A:
    print("Normal")
elif H < A:
    print("Deficiency")
else:
    print("Excess")