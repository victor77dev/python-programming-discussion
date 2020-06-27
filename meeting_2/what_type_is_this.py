def what_type_is_this(variable):
    # Let's try debugger
    what_type_is_this.line += 1
    print(f'line {what_type_is_this.line}: {variable} is ', end='')
    print(f'{type(variable).__name__}')
what_type_is_this.line = 7

what_type_is_this(42) #integer
what_type_is_this(3.14) #float
what_type_is_this(42.) #float
what_type_is_this(1/3) #float
what_type_is_this(1//3) #integer
what_type_is_this(2//3) #integer
what_type_is_this('Coding') #string
what_type_is_this('Don\'t panic') #string
what_type_is_this(1/3*3 == 1) # true, boolean
what_type_is_this(True) #true, boolean
what_type_is_this(0 == True) # false, boolean
what_type_is_this(0 == False) #true, boolean
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
what_type_is_this(1 < 3 < 4)
what_type_is_this(2 == 2 is True)
a = -1; what_type_is_this(a)
what_type_is_this(abs(a))
a = 'Haha'; what_type_is_this(a)
a = ['Haha', 1]; what_type_is_this(a)
what_type_is_this(abs(a))
