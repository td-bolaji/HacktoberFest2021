
def fibonacci(n):
    """
    Return n-th Fibonacci number.
    Raises TypeError if n is not integer.
    Raises ValueError if n is negative.
    :param n: (int) natural number
    :return: (int) n-th Fibonacci number
    """
    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2, n + 1):
            c = a + b
            a, b = b, c
        return b


def run():
    num = int(input('Enter the n-th Fibonacci number you want to get: '))
    check(num)
    print(fibonacci(num))


def check(t):
    if type(t) != int:
        print('Please enter a NUMBER')
        run()


run()
