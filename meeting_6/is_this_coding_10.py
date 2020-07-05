def is_this_coding(activity = None):
    if activity == None:
        activity = input('What do you want to check?\nPlease input: ')

    if activity == 'Typing':
        print(f'No! Of course not! {activity} is not Coding.')
    elif activity == 'Programming' or activity == 'Coding':
        print(f'Yes! {activity} is Coding.')
    elif activity == 'Debugging':
        print(f'Yes! {activity} is part of Coding.')
    else:
        print(f'What is that? {activity}???')

for i in range(10):
    is_this_coding()
# is_this_coding('Typing') # No! Of course not!
# is_this_coding('Programming') # Yes!
# is_this_coding('Coding') # Yes!
# is_this_coding('Cooking') # What is that?
# is_this_coding('Debugging') # What is that?
