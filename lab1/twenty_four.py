from random import randint


def solver(digits, results):
    print(digits)


def main():
    digits = []
    for i in range(4):
        digits.append(randint(1,13))
    solver(digits, 0)

if __name__ == "__main__":
    main()