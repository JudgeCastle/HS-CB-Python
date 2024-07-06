count = 0
deposit = int(input())

while True:
    if deposit >= 50000 and deposit <= 700000:
        interest = deposit * .071
        deposit = interest + deposit
        count += 1
    else:
        print(count)
        break