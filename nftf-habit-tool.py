import webbrowser
import time
import sys

def getNFTF():
    x = input()
    x = int(float(x))
    while x < -5 or x > 5:
        print('You did not choose a valid number. Try again.')
        x = input()
        x = int(float(x))
    return x
    

print('What is the habit you want to form?')
habit = input()

print(habit + ' sounds like a good idea - but let us make sure it is the right decsion for you.')
print('Please respond to the following questions on a scale of -5 to 5 where')
print('0 means you feel truly neutral about the subject.')

print(' ')
print('Are you ready to start? (Yes or No)')

start = input()

if start == 'y' or start == 'Y' or start == 'Yes' or start == 'yes' or start == 'ye' or start =='Ye':
    print('Great, let us get to it.')
    
else:
    print('Looks like you are not ready yet.')
    print('Perhaps you can check out my blog on the Negative Five to Five Scale.')
    print('Redirecting you now...')
    time.sleep(3)
    webbrowser.open_new_tab("http://www.salimahismail.com/read/nftf")
    sys.exit() 

print(' ')
print('Question 1: How excited are you to start ' + habit)
print('-5 means not at all excited.')
print('0 means you feel neutral about it.')
print('+5 means extremely excited.')

excitementResponse = getNFTF()

def questExcite(excitement):
    if int(excitement) < 0 and int(excitement) >= -5:
        print('If you are not excited about forming this habit, why bother?')
        print('Life is too short to start something you are not excited about.')
        print('I recommend you think of something other than ' + habit)
        print('that has similar benefits, but actually excites you.')
        print(' ')
        time.sleep(2)
        print('Goodbye! Come back when you are ready to try again!')
        print('Please let me know what you thought of this process.')
        print('Redirecting you now...')
        time.sleep(3)
        webbrowser.open_new_tab("http://www.salimahismail.com/contact")
        sys.exit()

    elif int(excitement) == 0:
        print('It is not ideal that you feel neutral about this, but we will continue.')

    elif int(excitement) > 0 and int(excitement) <= 5:
        print('It is great to see that you are excited about '+ habit +'.')
        print('This is a prosperous start.')

questExcite(excitementResponse)

time.sleep(1)
print(' ')
print('Question 2: What level of mental health benefits or detriments do you expect from ' + habit + '?')
print('-5 means it will take a major mental health toll.')
print('0 means no benefits but also no detriments.')
print('+5 means huge mental health benefits.')

mhResponse = getNFTF()

intTotal = int(excitementResponse) + int(mhResponse)

def questInt1(totalOne):
    if int(totalOne) < 0:
        print('Your excitement about ' + habit +' does not counteract the mental health toll it will impose on you.')
        print('I recommend you think of something other than ' + habit)
        print('that has similar benefits, but will not be so mentally tough.')
        print(' ')
        time.sleep(2)
        print('Goodbye! Come back when you are ready to try again!')
        print('Please let me know what you thought of this process.')
        print('Redirecting you now...')
        time.sleep(3)
        webbrowser.open_new_tab("http://www.salimahismail.com/contact")
        sys.exit()

    elif int(totalOne) == 0:
        print('Currently, your excitement balances the mental health toll of ' + habit + '.')
        print('Let us see if we can determine other benefits.')

    elif int(totalOne) > 0:
        print('So far, ' + habit + ' is seeming like a good idea. Great!')

questInt1(intTotal)

time.sleep(1)
print(' ')
print('Question 3: What level of physical health benefits or detriments do you expect from ' + habit + '?')
print('-5 means it will take a major physical health toll.')
print('0 means no benefits but also no detriments.')
print('+5 means huge physical health benefits.')

phResponse = getNFTF()    
      
int2Total = int(intTotal) + int(phResponse)

def questInt2(totalTwo):
    if int(totalTwo) < 0:
        print('The physical toll of ' + habit +' is stronger than its mental health benefits and')
        print('your excitement about it combined.')
        print('I recommend you think of something other than ' + habit)
        print('that has similar benefits, but will not be so physically draining.')
        print(' ')
        time.sleep(2)
        print('Goodbye! Come back when you are ready to try again!')
        print('Please let me know what you thought of this process.')
        print('Redirecting you now...')
        time.sleep(3)
        webbrowser.open_new_tab("http://www.salimahismail.com/contact")
        sys.exit()

    elif int(totalTwo) == 0:
        print('Your excitement and mental health benefits of ' + habit + ' balances any potential physical toll.')
        print('Let us see if we can determine other benefits.')

    elif int(totalTwo) > 0:
        print('Wow, ' + habit + ' is netting positive - this is a good thing!')

questInt2(int2Total)

time.sleep(1)
print(' ')
print('Question 4: What level of finacial benefits or costs do you expect from ' + habit + '?')
print('-5 means it will cost a lot of money to take on this habit.')
print('0 means no cost.')
print('+5 means this habit will either make you money or increase your earning potential.')

moneyResponse = getNFTF() 

int3Total = int(int2Total) + int(moneyResponse)

def questInt3(totalThree):
    if int(totalThree) < 0:
        print('The financial burden of ' + habit +' is stronger than its physical health, mental health benefits and')
        print('your excitement about it combined.')
        print('I recommend you think of something other than ' + habit)
        print('that has similar benefits, but will not be so financially cumbersome.')
        print(' ')
        time.sleep(2)
        print('Goodbye! Come back when you are ready to try again!')
        print('Please let me know what you thought of this process.')
        print('Redirecting you now...')
        time.sleep(3)
        webbrowser.open_new_tab("http://www.salimahismail.com/contact")
        sys.exit()

    elif int(totalThree) == 0:
        print('The scores you assigned to your excitement and physical and mental health benefits of ' + habit + ' neutralizes any financial cost.')
        print('Let us see if we can determine other benefits.')

    elif int(totalThree) > 0:
        print('Even after all these questions, ' + habit + ' is scoring well!')

questInt3(int3Total)

time.sleep(1)
print(' ')
print('Question 5: What level of time benefits or sacrifices do you expect to make for ' + habit + '?')
print('-5 means it will take a lot of your time to participate in this habit.')
print('0 means you will not have to sacrifice anything to make time for this habit.')
print('+5 means it will save you lots and lots of time.')

timeResponse = getNFTF() 

int4Total = int(int3Total) + int(timeResponse)

if int(int4Total) < 0:
    print('The time burden of ' + habit +' is stronger than all the other benefits we have discussed so far.')
    print('I recommend you think of something other than ' + habit)
    print('that has similar benefits, but will not be such a time sink.')
    print(' ')
    time.sleep(2)
    print('Goodbye! Come back when you are ready to try again!')
    print('Please let me know what you thought of this process.')
    print('Redirecting you now...')
    time.sleep(3)
    webbrowser.open_new_tab("http://www.salimahismail.com/contact")
    sys.exit()

elif int(int4Total) == 0:
    print('At this point, it seems like ' + habit + ' will not have a major effect in any way on your life.')
    print('Proceed at you own discreation')
    

elif int(int4Total) > 0:
    print('I pleased to inform you that ' + habit + ' seems like it will have a net positive in your life.')
    print('A +' + str(int4Total) + ' effect. To be precise.')
    
print('Please let me know what you thought of this process.')
print('Redirecting you now...')
time.sleep(3)
webbrowser.open_new_tab("http://www.salimahismail.com/contact")
sys.exit() 




