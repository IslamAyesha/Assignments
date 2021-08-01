import random as r
import string
length = 6
OTP = ' '
characters = string.ascii_letters + string.digits
for i in range(length):
    OTP = OTP + r.choice(characters)
print('OTP:',OTP)