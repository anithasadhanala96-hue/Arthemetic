
import sys
input1=sys.argv[1].upper()
input2=sys.argv[2].upper()
A='ROCK'
B='PAPER'
C='SCISSOR'
if(input1==A and input2==B):
   print("paper wins rock lost")
elif(input1==A and input2==C):
   print("rock wins & scissor lost")
elif(input1==A and input2==A):
    print("TIE")  
elif(input1==B and input2==A):
    print("paper wins rock lost")
elif(input1==B and input2==C):
    print("scissor wins & paper lost")
elif(input1==B and input2==B):
    print("TIE")  
elif(input1==C and input2==A):
    print("rock wins & scissor lost")  
elif(input1==C and input2==B):
    print("scissor wins & paper lost")
elif(input1==C and input2==C):
    print("TIE")  
else:
    print("give proper input")    

