def foo_bar_ext(N):
    for i in range(1, N + 1):
        string = ""
        # Check 1
        if i % 3 == 0:
            string += "aaa"
        # Check 2
        if i % 5 == 0:
            string += "bbb"
        # Check 3
        if i % 7 == 0:
            string += "ccc"
        # Check 4
        if i % 11 == 0:
            string += "ddd"

        if string == "":
            # Step 5
            print(i)
        else:
            # Step 6
            print(string)

foo_bar_ext(1650)
