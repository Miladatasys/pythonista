# A parameter is a variable which we use in the function def. 
# It is a "handle" that allows the code in the function to access the args for a particular function invocation
def thing():
    print('Hello')
print('There')

def func(x) :
    print(x)

func(10)
func(20)

def stuff() :
    print('Hello')
    return
print('World')

stuff()

def greet(lang) :
    if lang ==  'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        return 'Hello'
print(greet('fr'), 'Michael')

def addtwo(a, b):
    added = a + b
    return a
x = addtwo(2, 7)
print(x)