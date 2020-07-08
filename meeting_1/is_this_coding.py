def is_this_coding(activity):
    if activity == 'Typing':
        print('No! Of course not!')
    elif activity == 'Programming' or activity == 'Coding':
        print('Yes!')
    else:
        print('What is that?')

is_this_coding('Typing') # No! Of course not!
is_this_coding('Programming') # Yes!
is_this_coding('Coding') # Yes!
is_this_coding('Cooking') # What is that?
