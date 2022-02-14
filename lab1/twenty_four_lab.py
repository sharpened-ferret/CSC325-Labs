import time
from itertools import combinations
from random import randint

global_store = []

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

def calc_to_string(calc_history, calc):
    op_str = ""
    match calc[1]:
        case "+":
            op_str = "add"
        case "-":
            op_str = "sub"
        case "*":
            op_str = "mul"
        case "/":
            op_str = "div"

    return "{}({}{}{}); ".format(calc_history, calc[0], op_str, calc[2])

def solve(digits, goal, calcs, all_values):

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
                return_val = calc_to_string(calcs, result_calcs[n])
                if all_values:
                    global_store.append(return_val)
                else: 
                    return return_val
        return False
    
    # Gets all possible pairs of numbers
    pairs = list(combinations(digits, 2))
    for pair in pairs:
        check_result, check_calcs = combine(pair[0], pair[1])
        for i, result in enumerate(check_result):
            calc = check_calcs[i]
            new_digits = digits.copy()

            # Gets the positions of the digits used
            a_pos = new_digits.index(pair[0])
                        
            new_digits.pop(a_pos)

            b_pos = new_digits.index(pair[1])
            new_digits.pop(b_pos)
            new_digits.append(result)

            calc_str = calc_to_string(calcs, calc)

            recurr = solve(new_digits, goal, calc_str, all_values)
            if recurr:
                return recurr
            else:
                continue

def main():
    digits = []
    for i in range(6):
        digits.append(randint(1,13))

    time_one = time.time()
    single_result = solve(digits, goal=24, calcs="", all_values=False)
    time_two = time.time()
    solve(digits, goal=24, calcs="", all_values=True)
    time_three = time.time()

    single_runtime = time_two - time_one
    print("----Single Result----\nInput: {}\nFound Solution: {}\nRuntime: {}s\n".format(
        digits,
        single_result, 
        single_runtime))

    exhaustion_runtime = time_three - time_two
    print("---Exhaustion Result---\nInput: {}\nFound Solution(s): ".format(
        digits,))
    for result in global_store:
        print(result)
    print("Runtime: {}s".format(exhaustion_runtime))


if __name__ == "__main__":
    main()

"""
Task 2:

Changes to a, b, or M should have a minimal effect on the program performance,
however, increases in n will have a significant effect, since the program loops
over all possible pairs of digits in n, so increases with n((n(n-1))/2)
"""