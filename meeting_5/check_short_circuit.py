def always_true(called):
    print(f'always_true is called!!!')
    called[0] += 1
    print(f'in function called: {called}')
    return True

def always_false(called):
    print(f'always_false is called!!!')
    called[0] += 1
    print(f'in function called: {called}')
    return False

def replace_with_func(str):
    str = str.replace('T', 'always_true(called)')
    str = str.replace('F', 'always_false(called)')
    return str

def check_short_circuit(statement):
    called = [0]
    print(f'Let\'s check {statement}.')
    print(replace_with_func(statement))

    result = eval(replace_with_func(statement))
    
    # # example
    # check_short_circuit("T or T")
    # # step 1
    # replace_with_func return string => "always_true(called) or always_true(called)"
    # # step 2
    # eval convert string to statement => result = always_true(called) or always_true(called)
    # # step 3
    # always_true() return True => result = True or True

    print(f'outside function called: {called}')
    short_circuited = 'This is short circuited' if (called[0] == 1) else 'Both functions are called'
    print(f'{statement} is {result}. {short_circuited}.\n')

check_short_circuit('T or T')
check_short_circuit('F or T')
# check_short_circuit('T or F')
# check_short_circuit('F or T')
# check_short_circuit('F or F')

# check_short_circuit('T and T')
# check_short_circuit('T and F')
# check_short_circuit('F and T')
# check_short_circuit('F and F')
