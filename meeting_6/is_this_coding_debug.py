def is_this_coding(activity):
    if activity == 'Typing':
        print(f'No! Of course not! {activity} is not Coding.')
    elif activity == 'Programming' or activity == 'Coding':
        print(f'Yes! {activity} is Coding.')
    elif activity == 'Debugging':
        print(f'Yes! {activity} is part of Coding.')
    else:
        print(f'What is that? {activity}???')

is_this_coding('Typing') # No! Of course not! Typing is not Coding.
is_this_coding('Programming') # Yes! Programming is Coding.
is_this_coding('Coding') # Yes! Coding is Coding.
is_this_coding('Cooking') # What is that? Cooking???
is_this_coding('Debugging') # Yes! Debugging is part of Coding.
