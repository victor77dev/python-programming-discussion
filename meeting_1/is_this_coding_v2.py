def is_this_coding(activity):
    if activity == 'Typing':
        print('No! Of course not! ' + activity + ' is not Coding!')
    elif activity == 'Programming' or activity == 'Coding':
        print(f'Yes! {activity} is Coding!')
    else:
        print(f'What is that? {activity} == Coding???')

is_this_coding('Typing')
is_this_coding('Programming')
is_this_coding('Coding')
is_this_coding('Cooking')