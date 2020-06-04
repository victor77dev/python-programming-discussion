def isthiscoding(c):
    a = ['Typing','Programming','No! Of course not!','Coding','What is that?']
    if c == a[0]:
        print(a[2])
    elif c == a[1] or c == a[3]:
        print('Yes!')
    else:
        print(a[4])

isthiscoding('Typing') # No! Of course not!
isthiscoding('Programming') # Yes!
isthiscoding('Coding') # Yes!
isthiscoding('Cooking') # What is that?
