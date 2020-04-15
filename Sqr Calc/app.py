from math import *

while 1 == 1:
    # Asks user to enter vars
    a = int(input("Введите a "))
    b = int(input("Введите b "))
    c = int(input("Введите c "))
    # Counts then prints discriminant
    disc = b * b - 4 * a * c
    print("\nДискриминант = " + str(disc))
    # Checks if discriminant is less then 0, if true - equation has no roots
    if disc < 0:
        print("\nУравнение не имеет корней")
        input("\nНажмите Enter для продолжения\n")
    else:
        # Checks if discriminant is equal to 0, if true - equation has only one root
        if disc == 0:
            x = -b / (2 * a)
            print("\nx = " + str(x))
            input("\nНажмите Enter для продолжения\n")
        else:
            # Squares  discriminant
            discsq = sqrt(disc)
            # Counts then prints roots
            x1 = (-b + discsq) / (2 * a)
            x2 = (-b - discsq) / (2 * a)
            print("\nx1 = " + str(x2) + "\nx2 = " + str(x1))
            input("\nНажмите Enter для продолжения\n")
