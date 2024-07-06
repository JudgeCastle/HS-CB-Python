def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    answer_1 = str("1. To repeat a statement multiple times.")
    answer_2 = str("2. To decompose a program into several small subroutines.")
    answer_3 = str("3. To determine the execution time of a program.")
    answer_4 = str("4. To interrupt the execution of a program.")
    correct_answer = 2
    print("Let's test your programming knowledge.")
    print("Why do we use methods?", answer_1, answer_2, answer_3, answer_4, sep=" ")

    while int(input("Please enter a number 1 - 4 to select your answer.")) != correct_answer:
        print("Incorrect. Please try again.")
    else:
        print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
