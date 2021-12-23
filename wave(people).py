"""
Task

In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 

Rules

 1.  The input string will always be lower case but maybe empty.

 2.  If the character in the string is whitespace then pass over it as if it was an empty seat

Example

wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

"""

def wave(people):
    # Code here
    res = []
    string = ''.join(people.split(' '))
    for idx in range(len(string)):
        s = ''
        for i, c in enumerate(people):
            if c != ' ':
                if idx == i :
                    s += people[i].capitalize()
                else:
                    s += c 
        res.append(s)
    print(res)
    return res

wave('helloworld')