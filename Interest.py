
import sys 
p=int(sys.argv[1])
t=int(sys.argv[2])
r=int(sys.argv[3])
def interestfunction():
    return (p*t*r)/100
print('principal' ,p ,'time', t, 'rate of interest',r,interestfunction())  