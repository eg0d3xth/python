import random
r = random
number = r.randint(0, 100)

guess = 0

while guess != number:
    guess = int(input("Введите чило: "))
    if guess < number:
        print("\nЧисло больше\n")
    elif guess > number:
        print("\nЧисло меньше\n")

if guess == number:
    print("\nВы выиграли!")
    input("\nНажмите Enter что бы выйти")
