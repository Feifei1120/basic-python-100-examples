def max_age_cal(age):
    return max(age)

def min_age_cal(age):
    return min(age)

def age_cal(*args):
    print(args)
    max_age = max_age_cal(args)
    min_age = min_age_cal(args)

    print(max_age)
    print(min_age)

    return max_age, min_age

age_cal(20,25,30,33,28)