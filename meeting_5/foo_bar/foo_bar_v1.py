def foo_bar(N):
    for i in range(1, N + 1):
        output = ""
        if i % 3 == 0:
            output += "Foo"
        if i % 5 == 0:
            output += "Bar"
        if i % 3 != 0 and i % 5 != 0:
            output = i
        print(output)

foo_bar(100)
foo_bar(42)

