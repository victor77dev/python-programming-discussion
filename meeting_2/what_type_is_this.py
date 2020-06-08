def what_type_is_this(variable):
    # Let's try debugger
    print(f'{variable} is ', end='')
    print(f'{type(variable)}')

what_type_is_this(42)
what_type_is_this(3.14)
what_type_is_this(42.)
what_type_is_this(1/3)
what_type_is_this(1//3)
what_type_is_this(2//3)
what_type_is_this('Coding')
what_type_is_this('Don\'t panic')
what_type_is_this(1/3*3 == 1)
what_type_is_this(True)
what_type_is_this(0.1 + 0.2 == 0.3)
a = -1
what_type_is_this(a)
what_type_is_this(abs(a))
a = 'Haha'
what_type_is_this(a)
a = ['Haha', 1]
what_type_is_this(a)
what_type_is_this(abs(a))
