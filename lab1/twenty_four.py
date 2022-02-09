from itertools import combinations
from random import randint

def combine(a, b):
    values = [a+b, a*b]
    calculations = [(a, "+", b), (a, "*", b)]

    if b > a:
        values.append(b-a)
        calculations.append((b, "-", a))
    else:
        values.append(a-b)
        calculations.append((a, "-", b))
    if b != 0:
        values.append(a/b)
        calculations.append((a, "/", b))
    if a != 0:
        values.append(b/a)
        calculations.append((b, "/", a))
    return values, calculations

def calc_to_string(calc):
    print(calc)
    return "{} {} {}".format(calc[0], calc[1], calc[2])

def solve(digits, goal, calcs):

    # On first run, populate calculations array
    if calcs == []:
        for i in range(len(digits)):
            calcs.append(str(digits[i]))
        print(calcs)
    # If there is only one number is provided, check if it equals goal
    if len(digits) == 1:
        if digits[0] == goal:
            return digits[0]
        else:
            return False
    # If only two numbers are left, combine them and check results
    if len(digits) == 2:
        results, result_calcs = combine(digits[0], digits[1])
        for n,result in enumerate(results):
            if result == goal:
                return calc_to_string(result_calcs[n])
        return False
    
    # Gets all possible pairs of numbers
    pairs = list(combinations(digits, 2))
    for pair in pairs:
        check_result, check_calcs = combine(pair[0], pair[1])
        for i, result in enumerate(check_result):
            calc = check_calcs[i]
            
            calc_str = calc_to_string(calc)
            new_digits = digits.copy()
            new_calcs = calcs.copy()

            # Gets the positions of the digits used
            a_pos = new_digits.index(pair[0])
            
            str_form = "Popping {}, val {}"
            print(str_form.format(pair[0], new_digits[a_pos]))
            new_digits.pop(a_pos)
            new_calcs.pop(a_pos)

            b_pos = new_digits.index(pair[1])
            print(str_form.format(pair[1], new_digits[b_pos]))
            new_digits.pop(b_pos)
            new_digits.append(result)

            
            new_calcs.pop(b_pos)
            new_calcs.append(calc_str)
            print(new_calcs)
            print(new_digits)
            
            recurr = solve(new_digits, goal, new_calcs)
            if recurr:
                return recurr
            else:
                continue



def main():
    digits = []
    for i in range(4):
        digits.append(randint(1,13))
    print(solve(digits, goal=24, calcs=[]))


if __name__ == "__main__":
    main()