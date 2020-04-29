# This is my original work and shall not be copied and used anywhere without my prior approval. 
# This bidding game is a guessing game played by one human contestant and 3 computer contestants to determine
# the price of a given object in range 50 to 1000.
# closest bid wins the game. if human contestant looses the game, he is given one last chance.


print("Welcome to the bidding game")
contestantNumber1=input("Please enter your name using only letters: ")
# Throw error if human contestant name is not all alphabets
nameCheck=True
for i in contestantNumber1:
    if i.isalpha()==False:
        nameCheck=False
if nameCheck==False:
    contestantNumber1=input("Please only use letters when filling in your name tag")
a=len(contestantNumber1)
contestantNumber1=contestantNumber1[0].upper()+contestantNumber1[1:a].lower()
print(contestantNumber1+"! Come on down! you're the next contestant on the Price is (sorta) Right!")

presenterName="Bob Meower"

# enter name of the computer contestants
contestantNumber2=input("please enter player no. 2 name")
contestantNumber3=input("please enter player no. 3 name")
contestantNumber4=input("please enter player no. 4 name")

print(presenterName+" welcomes "+contestantNumber1+" to contestant's row, joining ",
      contestantNumber2,",",contestantNumber3,"and",contestantNumber4)
winnerStatus="wrong"

#generate object value
import random
p1=random.randint(50,1001)
#print(p1)
print(presenterName,"shows you the prize you will be bidding on for value upto 1000")

# define function to be called for actual play
def strike(winnerStatus):
    
    b1=input(contestantNumber1+", what is your bid? $")
    while str(b1).isdecimal()==False:
        b1=input("please enter a numerical postive value")
    while not b1>"0":
        print("i'm sorry I couldn't make that out , a bid of at least $1 please")
        b1=input(contestantNumber1+" what is your bid? $")
    
    for i in range(1):
        b2=random.randint(50,1001)
        b3=random.randint(50,1001)
        b4=random.randint(50,1001)
        
        print(contestantNumber2,"bids",b2,"dollars.")
        print(contestantNumber3,"bids",b3,"dollars.")
        print(contestantNumber4,"bids",b4,"dollars.")
        l2=[p1]
        l1=[int(b1),b2,b3,b4]
        #print(l1)
        # make list of difference of bid amounts to actual amount
        for i in range(len(l1)):
            l1[i]=l1[i]-l2[0]
        #print(l1)
        d=False
        for i in l1:
           d=i<0
           if d==True:
               break
        if d==True:
            print(presenterName," says, Everyone has bid too high, lets try again")
        #print(d)
        d1=abs(l1[0])
        d2=abs(l1[1])
        d3=abs(l1[2])
        d4=abs(l1[3])
        l2=[d1,d2,d3,d4]
        print("closest differnce with bid is $",min(l2))
        if min(l2)==d1:
            print(presenterName,"says, ",contestantNumber1,"is the winner!")
            winnerStatus=contestantNumber1
            print(winnerStatus)
        elif min(l2)==d2:
            print(presenterName,"says, ",contestantNumber2,"is the winner!")
        elif min(l2)==d3:
            print(presenterName,"says, ",contestantNumber3,"is the winner!")
        else:
            print(presenterName,"says, ",contestantNumber4,"is the winner!")   
    #print(winnerStatus)
    return winnerStatus
    
#call function for starting the game
winnerStatus=strike(winnerStatus)

#print(winnerStatus)
#print(type(winnerStatus))

# give one more chance to human contestant
if winnerStatus=="wrong":
    print(contestantNumber1,"You have one last chance")
    winnerStatus=strike(winnerStatus)
    print(presenterName," says, The actual price of the item was", p1," dollars")
    if winnerStatus=="wrong":
        print(presenterName," turns to",contestantNumber1,"and says, i'm sorry you didnt have better luck here today, but we're sending you home with the unofficial board game of the price is (sorta) right")
    else:
        print("Congratulations",contestantNumber1,"you have won the game")
else:
    print("Congratulations",contestantNumber1,"you have won the game")





