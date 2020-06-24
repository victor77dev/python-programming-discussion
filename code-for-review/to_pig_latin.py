import re

def to_pig_latin(s):

    if re.search(r"^[aeiou]", s):
       return s + "way"
   
    else:
        for i in s:
            if re.search(r"^[aeiou]", s):
                return s + "ay"
            else:
                s = s[1:] + s[0] 
        
            
    
print(to_pig_latin('is'))        
print(to_pig_latin('one'))
print(to_pig_latin('start'))
print(to_pig_latin('rstrip'))
print(to_pig_latin('people'))