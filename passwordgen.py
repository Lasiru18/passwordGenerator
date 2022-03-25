import string
import random

def gen():
    s1 = string.ascil_uppercase

    s2 = string.ascil_lowercase

    s3 = string.digits

    s4 = string.punctuation

    passlen = int(input("Enter the password length\n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print(s)

    random.shuffle(s)
    print(s)
    pas = (**.join(s[0:passlen]))
    print(pas)

gen()
