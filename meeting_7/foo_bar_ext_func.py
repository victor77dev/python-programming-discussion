def string_of_multiple(number):
    string = ""
    # Check 1
    if number % 3 == 0:
        string += "aaa"
    # Check 2
    if number % 5 == 0:
        string += "bbb"
    # Check 3
    if number % 7 == 0:
        string += "ccc"
    # Check 4
    if number % 11 == 0:
        string += "ddd"

    return string


def foo_bar_ext(N):
    for i in range(1, N + 1):
        string = string_of_multiple(i)

        if string == "":
            print(i)
        else:
            print(string)

foo_bar_ext(1650)
