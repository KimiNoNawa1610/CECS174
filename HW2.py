
def menu():
        x=input('Please choose the program you want to work with')
        print('A.Check a palindrome')
        print('B.Check a word square')
        print('C.Quit')
        return x
def menu_chocie(x):
    while True:
        if x=='A':
            return A
        elif x=='B':
            return B
        elif x=='C':
            print('Thank for using our calculation. See you later.')
            return 'end'
        else:
            print('Please select the correct program')
def get_pharse():
    while True:
        pharse=input('Please enter an English pharse')
        if pharse.isdigit() is True or len(pharse.strip())==0:
            print('I do not understand')
        else:
            return pharse
def is_palindrome(pharse):
    pharse=pharse.lower()
    pharse=''.join([char for char in pharse if char.isalpha()])
    length=len(pharse)
    print(pharse)
        

    
    

    
    
    
