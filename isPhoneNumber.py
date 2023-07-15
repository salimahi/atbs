from itertools import chain

def isPhoneNumber(text):
    if len(text) > 13 or len(text) < 10 or len(text) == 11:
        return False
    elif len(text) == 13:
        if text[0] !='(' or text[4] !=')' or text[8] !='-':
            for i in chain(range(1,3), range(5,7), range(9,12)):
                if text[i].isdecimal():
                    return False
        else:
            return True

    elif len(text) == 12:
        if text[3] !='-' or text[7] !='-':
            for i in chain(range(0,2), range(4,6), range(8,11)):
                if not text[i].isdecimal():
                    return False
        else:
            return True

    elif len(text) == 10:
        if not text.isdecimal():
            return False
        else:
            return True
    
##print(isPhoneNumber('(647)858-7212')) #T
##print(isPhoneNumber('647-858-7212')) #T
##print(isPhoneNumber('6478587212')) #T
##print(isPhoneNumber('64785872120')) #F
##print(isPhoneNumber('6478587212000')) #F
##print(isPhoneNumber('abcdefghij')) #F

message = 'Call me for a good time at 4433938765 or at (443)654-0987 or at 212-543-5968. You can also call at 3214567890 or (333)222-4432'

for i in range(len(message)):
    chunk10 = message[i:i+10]
    chunk12 = message[i:i+12]
    chunk13 = message[i:i+13]
    if isPhoneNumber(chunk10):
        print(f"Phone number found:{chunk10}")
    if isPhoneNumber(chunk12):
        print(f"Phone number found:{chunk12}")
    if isPhoneNumber(chunk13):
        print(f"Phone number found:{chunk13}")
print('Phone number search complete')
