import random

fortune = ['For Sure',
           'Definitely Yes',
           'Yes but should be No',
           'No but should be Yes',
           'Definitely No',
           'Maybe',
           'What do you think?',
           'Forget it and do something chaotic',
           'No no no no no no no no no no no x 100000']

print(fortune[random.randint(0, len(fortune) -1)])
