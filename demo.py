"""Demo script for Entire trial - triggers a Code review agent run."""


def greet(name):
    return "Hello, " + name + "!"


def add(a, b):
    return a + b


def main():
    print(greet("Entire"))
    print("2 + 3 =", add(2, 3))


if __name__ == "__main__":
    main()
