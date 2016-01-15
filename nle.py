'''This program will calculate the flow profiles of a thin film surrounded by flowing air.'''

#import relevant libraries
import numpy as np
import matplotlib.pyplot as plt

#input constants

#width of film = 2*a
a = 50
#height of air channel on top of film = c
c = 100
#width of channel = b
b=50
#mu1

#mu2
beta = 55

#number of terms to keep = n
n=10
lam = b/a
gam = c/a
beta = 55
#define coefficient functions c1234
def fn(n):
    return 16.*(-1.)**n/(2.*n+1.)**3*np.pi**3

def kn(n):
    return (2.*n+1)*np.pi/2.

def c1(n, lam,gam,beta):
    top = fn(n)*(beta-beta/np.cosh( kn(n)/lam*gam ) -1)
    bot = (1-beta*np.tanh( -kn(n)/lam )*np.tanh( kn(n)/lam*gam ) )
    return top/bot

def c2(n,lam,gam,beta):
    
    return -c1(n,lam,gam,beta)*np.tanh(-kn(n)/lam)

def c3(n,lam,gam,beta):
    return c1(n,lam,gam,beta) -fn(n)*(beta -1)

def c4(n,lam,gam,beta):
    return beta*c2(n,lam,gam,beta)

def u1n(n,y,z,lam,gam,beta):
    return (fn(n) + c1(n,lam,gam,beta)*np.cosh(kn(n)/lam*y)+c2(n,lam,gam,beta)*np.sinh(kn(n)/lam*y))*np.cos(kn(n)*z)

def u2n(n,y,z,lam,gam,beta):
    return (beta*fn(n) + c3(n,lam,gam,beta)*np.cosh(kn(n)/lam*y)+c4(n,lam,gam,beta)*np.sinh(kn(n)/lam*y))*np.cos(kn(n)*z)
#Main Program

if __name__ == '__main__':
    nList = np.arange(0,n) #create list of integers from that we will run our sum on.

#Now, act on this array with numpy magic

#just do z = 0 to test this

    etagas = np.linspace(0,gam)
    etaliquid = np.linspace(-1,0)

    zeta = 0 #for test
    



