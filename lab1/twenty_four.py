from random import randint


def solver(digits):
    digits.sort()
    length = len(digits)
    highVal = digits[length-1]


def main():
    digits = []
    for i in range(4):
        digits.append(randint(1,13))
    print(solver(digits))

if __name__ == "__main__":
    main()