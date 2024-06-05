import random
import string
print("Welcome to password genrator")


lower=string.ascii_lowercase
upper=string.ascii_uppercase
digits=string.digits
symbols=string.punctuation


all=lower+upper+digits+symbols

password=random.sample(all,10)
password="".join(password)
print(password)