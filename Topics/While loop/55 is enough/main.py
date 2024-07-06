numbers = []

while True:
    num_input = int(input())
    if num_input == 55:
        break
    else:
        numbers.append(num_input)

count = len(numbers)
sum_amount = sum(numbers)
average = round(sum_amount / count)

print(count)
print(sum_amount)
print(average)
