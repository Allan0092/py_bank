import re
from faker import Faker


def check_email(_email):
    c=re.fullmatch("^[a-z]([a-z]*|[0-9]*)*@[a-z]*.[a-z]*",_email)
    return c 

def check_name(_name):
    c=re.fullmatch("[a-z]+",_name)
    return c

def check_password(_password):
    c=re.fullmatch("",_password)





if __name__=="__main__":
    id = Faker()

    for i in range(200):
        a=id.email()
        if check_email(a)==None:
            print(a)
        