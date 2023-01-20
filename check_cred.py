import re
from faker import Faker


def check_email(_email):
    c=re.fullmatch("^[a-z]([a-z]|[0-9])@[a-z].[a-z]",_email)
    return c 

def check_name(_name):
    c=re.fullmatch("[a-z]+",_name)
    return c

def check_password(_password):
    c=re.fullmatch("",_password)

def emptyfield_check(information):
    '''
        Checks if fields are empty
    '''
    for n,info in enumerate(information):
        if info=="" or info==None:
            if n==1:
                continue
            return True
    return False

def within_limit_check(information):
    '''
        checks if characters are within limit
    '''
    if len(information[0])<2 or len(information[0])>20:# first name
        return True
    if len(information[1])>20:# middle name
        return True
    if len(information[2])<2 or len(information[2])>20:# last name
        return True
    if len(information[3])<7 or len(information[0])>40:# email
        return True
    if len(information[4])<5 or len(information[4])>20:# username
        return True
    if len(information[5])<8 or len(information[0])>20:
        return True
    return False

def syntax_check(information):
    pass

def check_information(args):
    information=list(args)
    if emptyfield_check(information) and within_limit_check(information):
        return True
    return False

if name=="main":
    id = Faker()

    for i in range(200):
        a=id.email()
        if check_email(a)==None:
            print(a)

