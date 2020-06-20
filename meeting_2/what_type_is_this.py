def what_type_is_this(variable):
    # Let's try debugger
    what_type_is_this.line += 1
    print(f'line {what_type_is_this.line}: {variable} is ', end='')
    print(f'{type(variable).__name__}')
what_type_is_this.line = 8

# Please add the value and type output for each line (<value> is <type>) with comment
what_type_is_this(42) # 42 is int
what_type_is_this(3.14) # 3.14 is float
what_type_is_this(42.) # 42.0 is float
what_type_is_this(1/3) # 0.33 is float
what_type_is_this(1//3) # 0 is int
what_type_is_this(2//3) # 0 is int
what_type_is_this('Coding') # coding is str
what_type_is_this('Don\'t panic') # Don't panic is str
what_type_is_this(1/3*3 == 1) # true is bool # 1 == 1 is true
what_type_is_this(True) # true is bool
what_type_is_this(0 == True) # false is bool
what_type_is_this(0 == False) # true is bool
what_type_is_this(1 == True) # true is bool
what_type_is_this(1 == False) # false is bool
what_type_is_this(2 == True) # false is bool
what_type_is_this(2 == False) # false is bool
what_type_is_this(1 + True) # 2 is int # True = 1
what_type_is_this(True + True) # 2 is int # True = 1
what_type_is_this(1 + True == True) # false is bool
what_type_is_this((1 + True) == True) # false is bool
what_type_is_this(1 + (True == True)) # 2 is int
what_type_is_this((-1 + True) == True) # false is bool
what_type_is_this(-1 + (True == True)) # 0 is int
what_type_is_this(-1 + True == True) # false is bool
what_type_is_this((1 == 2 )!= 3) # true is bool
what_type_is_this(1 == 2 != 3) # false is bool # 1 == 2 and 2 != 3
what_type_is_this(1 == (2 != 3)) # true is bool
what_type_is_this((0 == 0) + False or True) # 1 is int # 1 + 0 is 1
what_type_is_this(0 == (0 + False) or True) # true is bool
what_type_is_this(0 == 0 + (False or True)) #  false is bool
what_type_is_this(0 == 0 + False or True) # true is bool
what_type_is_this(0.1 + 0.1 == 0.2) # true is bool
what_type_is_this(0.1 + 0.2 == 0.3) # false is bool # computer counts in binary, so decimals as base 2 fraction
what_type_is_this(1 < 3 < 4) # true is bool
what_type_is_this(2 == 2 is True) # false is bool
a = -1; what_type_is_this(a) # -1 is int
what_type_is_this(abs(a)) # 1 is int
a = 'Haha'; what_type_is_this(a) # Haha is str
a = ['Haha', 1]; what_type_is_this(a) # ['Haha, 1'] is list
what_type_is_this(abs(a)) # absolute on list?
what_type_is_this(abs(a))
