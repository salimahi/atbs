import random

#Cash on Hand
totalCash = 1000
doubleCash = 2*totalCash

#Start at Zero
bet = 0

#Setting up Tracking the Bet and Wheel Results
betList = []
wheelResults = []

#Either losing everything or doubling the money
while totalCash > 0 and totalCash < doubleCash:
        #Adding $5 each bet
        bet = bet + 5
        #Tracking the bet
        betList.append(bet)

        #Spinnging the roulette wheel
        wheel = random.randint(0,37)

        #Zero or Double Zero  Result
        if wheel == 0 or wheel == 37:
                wheelResults.append('zero')
                #Checking if you still have cash to bet with
                if totalCash >= bet:
                        totalCash = totalCash - bet
                elif totalCash < bet:
                        break
                

        #Landing on Red
        elif (wheel % 2) != 0:
                wheelResults.append('red')
                #Checking if you still have cash to bet with
                if totalCash >= bet:
                        totalCash = totalCash - bet
                elif totalCash < bet:
                        break
                
        #Landing on Black
        elif (wheel % 2) == 0:
                wheelResults.append('black')
                #Checking if you still have cash to bet with
                if totalCash >= bet + 5:
                        totalCash = totalCash + bet
                elif totalCash < bet + 5:
                        break

num_of_zeros = wheelResults.count('zero')
num_of_red = wheelResults.count('red')
num_of_black = wheelResults.count('black')

print(f"""You finished the game with a bet of {betList[-1]} and the result was {wheelResults[-1]}.
You are going home with ${totalCash}
Within the game, you hit:
0 or 00 {num_of_zeros} times
red {num_of_red} times
black {num_of_black} times.
""")

    

    
