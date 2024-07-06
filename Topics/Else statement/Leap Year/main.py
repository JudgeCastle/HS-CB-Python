year = int(input())

divisible1 = 4
divisible2 = 400
not_divisible = 100

if (year % divisible1 == 0 and year % not_divisible != 0) or year % divisible2 == 0:
    print("Leap")
else:
    print("Ordinary")