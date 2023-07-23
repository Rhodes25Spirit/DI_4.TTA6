import random

input_gender = input("Enter Gender (m/f): \n")
input_DOB = input("Enter Date of Birth (dd/mm/yyyy): \n")


def get_age(year, month, day):
    import datetime

    now = datetime.datetime.now()
    age = now.year - year
    if now.month < month:
        age -= 1
    elif now.month == month and now.day < day:
        age -= 1
    return age


def can_retire(gender, dob):
    yr_mon_day = dob.split("/")
    age = get_age(int(yr_mon_day[0]), int(yr_mon_day[1]), int(yr_mon_day[2]))
    if gender == "m" and age >= 67:
        return True
    elif gender == "f" and age >= 62:
        return True
    else:
        return False


if can_retire(input_gender, input_DOB) == True:
    print("You can retire")
else:
    print("You can't retire")


# Exercise 2

def sum(x):
    return (
        int(x)
        + int(str(x) + str(x))
        + int(str(x) + str(x) + str(x))
        + int(str(x) + str(x) + str(x) + str(x))
    )


print(sum(4))

# Exercise 3


def throw_dice():
    return random.randint(1, 6)


def throw_until_doubles():
    count = 0
    dice1 = throw_dice()
    dice2 = throw_dice()
    while dice1 != dice2:
        count += 1
        dice1 = throw_dice()
        dice2 = throw_dice()

    return count


print(throw_until_doubles())


def throw_100_doubles():
    count = 0
    for i in range(100):
        count += throw_until_doubles()
    average_to_reach_double = count / 100
    return count, average_to_reach_double


print(throw_100_doubles())
