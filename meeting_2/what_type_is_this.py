def what_type_is_this(variable):
    # Let's try debugger
    what_type_is_this.line += 1
    print(f'line {what_type_is_this.line}: {variable} is ', end='')
    print(f'{type(variable).__name__}')
what_type_is_this.line = 8

# Please add the value and type output for each line (<value> is <type>) with comment
what_type_is_this(42) # 42 is int
what_type_is_this(3.14)
what_type_is_this(42.)
what_type_is_this(1/3)
what_type_is_this(1//3)
what_type_is_this(2//3)
what_type_is_this('Coding') # Coding is str
what_type_is_this('Don\'t panic')
what_type_is_this(1/3*3 == 1)
what_type_is_this(True)
what_type_is_this(0 == True) # False is bool
what_type_is_this(0 == False)
what_type_is_this(1 == True)
what_type_is_this(1 == False)
what_type_is_this(2 == True)
what_type_is_this(2 == False)
what_type_is_this(1 + True)
what_type_is_this(True + True)
what_type_is_this(1 + True == True)
what_type_is_this((1 + True) == True)
what_type_is_this(1 + (True == True))
what_type_is_this((-1 + True) == True)
what_type_is_this(-1 + (True == True))
what_type_is_this(-1 + True == True)
what_type_is_this((1 == 2 )!= 3)
what_type_is_this(1 == 2 != 3)
what_type_is_this(1 == (2 != 3))
what_type_is_this((0 == 0) + False or True)
what_type_is_this(0 == (0 + False) or True)
what_type_is_this(0 == 0 + (False or True))
what_type_is_this(0 == 0 + False or True)
what_type_is_this(0.1 + 0.1 == 0.2)
what_type_is_this(0.1 + 0.2 == 0.3)
what_type_is_this(1 < 3 < 4) # True is bool
what_type_is_this(2 == 2 is True)
a = -1; what_type_is_this(a)
what_type_is_this(abs(a))
a = 'Haha'; what_type_is_this(a)
a = ['Haha', 1]; what_type_is_this(a)
what_type_is_this(abs(a))
