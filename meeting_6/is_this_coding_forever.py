def is_this_coding(activity = None):
    if activity == None:
        activity = input('What do you want to check?\nPlease input: ')

    if activity == 'exit':
        return True

    if activity == 'Typing':
        print(f'No! Of course not! {activity} is not Coding.')
    elif activity == 'Programming' or activity == 'Coding':
        print(f'Yes! {activity} is Coding.')
    elif activity == 'Debugging':
        print(f'Yes! {activity} is part of Coding.')
    else:
        print(f'What is that? {activity}???')

exit = False
while not exit:
    exit = is_this_coding()
    print('More') # This will be printed even user inputs exit

while True:
    if is_this_coding():
        break
    print('More') # This won't be printed after user inputs exit
