
import random
player=input("'R'for ROCK,'P'for paper,'S'for scissor:").upper()
computer=random.choice(['R','P','S'])
def playerwin():
    return "you wIn"
def computerwin():
    return"computer win"

if(player==computer and computer==player):
    print('TIE,TRY AGAIN')
elif(player=='P' and computer=='R' or player=='R' and computer=='S' or player=='S' and computer=='P'):
   print(playerwin())
elif(player=='R' and computer=='P' or player=='S' and computer=='R' or player=='P' and computer=='S'):
   print(computerwin())
else:
    print('please give proper input')   




