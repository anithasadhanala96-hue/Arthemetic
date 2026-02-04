count=1
import sys
tableendnumber=int(sys.argv[1])
tablenumber=int(sys.argv[2]) 

while(count<=tableendnumber):

   multiplicationoutput=count * tablenumber
   print(tablenumber,"x",count,"=",multiplicationoutput)
   count=count+1

