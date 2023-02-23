from faker import Faker
from datetime import datetime
from validate_email import validate_email

import DataActions


def valid_email(__email):
    """
        checks for valid email
    """

    is_valid = validate_email(__email)# checks if email is valid.
    if is_valid:# Is valid
        return True, -1, None
    return False, 3, ' not valid'

def valid_dob(__dob):
    """
        checks if given valid date of birth
    """
    if not __dob[-2:].isdigit() or __dob[-3]!='-' or not __dob[0].isdigit()or not __dob[-4].isdigit():#checks year, first digit and "-"
        return False, 4, ' not Valid'

    the_rest=__dob[:-3]
    length=len(the_rest)
    if length==3:# checks for "1-2"
        if the_rest[0].isdigit()==False or the_rest[1]!='-' or not the_rest[2].isdigit():
            return False, 4, ' not Valid'
    elif length==4:# checks for "1-23" or "12-3"
        if the_rest[1]=='-':
            if not the_rest[2].isdigit() or not the_rest[3].isdigit():
                return False, 4, ' not Valid'
        elif the_rest[2]=='-':
            if not the_rest[1].isdigit() or not the_rest[3].isdigit():
                return False, 4, ' not Valid'
        else:
            return False, 4, ' not Valid'
    elif length==5:# checks for "12-34"
        if the_rest[2]!='-':
            return False, 4, ' not Valid'
        if not the_rest[:2].isdigit() or not the_rest[3:5].isdigit():
            return False, 4, ' not Valid'
    return True, -1, None

def valid_username(__username):
    """
        checks if given valid username.
        username should contain letter, number, '_', '-', '@' and '.' 
    """
    for letter in __username:
        if not letter.isalnum():
            if letter not in ['_','-','@','.']:
                return False, 5, " not valid"
    return True, -1, None

def username_is_unique(info):
    """
        Checks if username is already taken.
    """
    all_users=DataActions.retrieve_all()# Gets all data from Account table.
    for user in all_users:# gets all information about a user sequentially.
        if user[6]==info:
            return False, 5, " already taken"
    return True, -1, None

def email_is_unique(info):
    """
        Checks if given email is already registered.
    """
    all_users=DataActions.retrieve_all()# Gets all data from Account table.
    for user in all_users:# gets all information about a user sequentially.
        if user[3]==info:# the email is already registered.
            return False, 3, " already taken"
    return True, -1, None

def valid_password(__passwrd):
    """
        checks if given valid password.
        A valid password must contain Uppercase, Lowercase, number and symbol.
    """
    variety=[False,False,False,False]# [Uppercase, Lowercase, number, symbol]
    for char in __passwrd:
        if char.isalpha():# checks for alphabet.
            if char.isupper():# checks for capital letter.
                variety[0]=True
            elif char.islower():# checks for small letter.
                variety[1]=True
        elif char.isdigit():# checks for digit.
            variety[2]=True
        elif char==' ':# checks for empty space.
            pass
        else:# the character is a symbol.
            variety[3]=True
    for v in variety:# checks if all criteria is met.
        if not v:# A criteria is not met.
            return False, 6, ' not valid'
    return True, -1, None

def both_passwords_match(information):
    """
        checks if both passwords match.
    """
    if information[6]==information[7]:# password and confirm password matches.
        return True, -1, None 
    else: # password and confirm password does not match.
        return False, 7, " does not match"

def emptyfield_check(information):
    '''
        Checks if any field is left empty.
    '''
    for n,info in enumerate(information):
        if info=="" or info==None or info=='None':
            if n==1:# middle name can be empty
                continue
            return False, n, ' cannot be empty'
    return True, -1, None

def within_limit_check(information):
    '''
        checks if characters are within character limit.
    '''
    if len(information[0])<2 or len(information[0])>20:# first name 
        return False, 0, ' must be between 2-20 letters'
    if len(information[1])>20:# middle name
        return False, 1, ' must be smaller than 20 letters'
    if len(information[2])<2 or len(information[2])>20:# last name
        return False, 2, ' must be between 2-20 letters'
    if len(information[3])<7 or len(information[0])>40:# email
        return False, 3, ' must be between 7-20 characters'
    if len(information[5])<5 or len(information[5])>20:# username
        return False, 5, " must be between 5-20 characters" 
    if len(information[6])<=8 or len(information[6])>20:# password
        return False, 6, " must be between 8-20 characters"
    return True, -1, None

def syntax_check(information):
    """
        checks if valid characters are given
    """
    for j in range(3):# First, middle and last name.
        for i in information[j]:
            _check=i.isalpha()# checks if it's alphabet.
            if not _check:
                return _check, j, ' can only have letters' 

    email_check=valid_email(information[3])# email checker.
    if not email_check[0]:
        return email_check
    
    dob_check=valid_dob(information[4])# date of birth checker.
    if not dob_check[0]:
        return dob_check
    
    username_check=valid_username(information[5])# username checker.
    if not username_check[0]:
        return username_check

    password_check=valid_password(information[6])# password checker.
    if not password_check[0]:
        return password_check

    conf_password_check=both_passwords_match(information)# if confirm password matches.
    if not conf_password_check[0]:
        return conf_password_check

    return True, -1, None

def is_unique_check(information:list):
    """
        Checks if username and email is already taken.
    """
    for_username=username_is_unique(information[5])
    for_email=email_is_unique(information[3])
    if not for_username[0]:
        return for_username
    elif not for_email[0]:
        return for_email
    else:
        return True, -1, None

def main(info):
    """
        main function.
        Arguments:
            first name : string
            middle name : string
            last name : string
            email id : string
            date of birth : string("d-m-yy")
            username : string
            password : string
            confirm password : string
            gender : string('male' | 'female' | 'other' | None)
    """
    
    check1=emptyfield_check(info)
    if check1[0]:
        check2=within_limit_check(info)
        if check2[0]:
            check3=syntax_check(info)
            if check3[0]:
                return is_unique_check(info)
            else:
                return check3
        else:
            return check2
    else:
        return check1

if __name__=="__main__":
    id = Faker()
    """for i in range(200):
            a=id.email()
            print(valid_email(a))"""