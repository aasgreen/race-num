'''This program will calculate the flow profiles of a thin film surrounded by flowing air.'''

#import relevant libraries
import numpy as np
import matplotlib.pyplot as plt

#input constants
test=0
def constants(test):
    if test==1:
        a=.1
        c=25.
        b=25./2.
        beta = .2/(18.6*10**(-6))

    if test ==0:
        a=np.longdouble(50.*10**(-3))
        b=np.longdouble(50.*10**(-3))
        c=np.longdouble(100.*10**(-3))
        beta = np.longdouble(55.)
    return a,b,c,beta
#width of film = 2*a
#a = .1
#height of air channel on top of film = c
#c = 25.
#width of channel = b
#b= 25./2.

#beta = mu_lc/mu_air

#beta = .2/(18.6*10**(-6))

#number of terms to keep = n
a,b,c,beta = constants(test)
n=100
lam = b/a
gam = c/a
n=100.
nList = np.arange(n)
#define coefficient functions c1234
def fn(n):
    return np.longdouble(16.*(-1.)**n/(2.*n+1.)**3*np.pi**3)

def kn(n):
    return np.longdouble((2.*n+1)*np.pi/2.)

def c1(n, lam,gam,beta):
    top = (beta-beta/np.cosh( kn(n)/lam*gam ) -1.)
    bot = (1-beta*np.tanh( -kn(n)/lam )*np.tanh( kn(n)/lam*gam ) )
    return fn(n)*(top/bot)

def c2(n,lam,gam,beta):
    top = (beta-beta/np.cosh( kn(n)/lam*gam ) -1.)
    bot = (1-beta*np.tanh( -kn(n)/lam )*np.tanh( kn(n)/lam*gam ) )

    return -fn(n)*(top/bot)*np.tanh(-kn(n)/lam)

def c3(n,lam,gam,beta):	
    #return c1(n,lam,gam,beta) -fn(n)*(beta -1.)
    top = (beta-beta/np.cosh( kn(n)/lam*gam ) -1.)
    bot = (1-beta*np.tanh( -kn(n)/lam )*np.tanh( kn(n)/lam*gam ) )
    return fn(n)*(top/bot+(1-beta))

def c4(n,lam,gam,beta):
    top = (beta-beta/np.cosh( kn(n)/lam*gam ) -1.)
    bot = (1-beta*np.tanh( -kn(n)/lam )*np.tanh( kn(n)/lam*gam ) )
    return fn(n)*(top/bot)*np.tanh(-kn(n)/lam)*beta

def u1n(n,y,z,lam,gam,beta):
    #return (fn(n) + c1(n,lam,gam,beta)*np.cosh(kn(n)/lam*y)+c2(n,lam,gam,beta)*np.sinh(kn(n)/lam*y))*np.cos(kn(n)*z)
    top = (beta-beta/np.cosh( kn(n)/lam*gam ) -1.)
    bot = (1-beta*np.tanh( -kn(n)/lam )*np.tanh( kn(n)/lam*gam ) )
    return (fn(n)*(1 + (top/bot)*( np.cosh( kn(n)*(y/lam) ) - 
        np.tanh( -kn(n)/lam )*np.sinh( kn(n)*(y/lam) ) )*np.cos(kn(n)*z) ) )


def u2n(n,y,z,lam,gam,beta):
    #return (beta*fn(n) + c3(n,lam,gam,beta)*np.cosh(kn(n)/lam*y)+c4(n,lam,gam,beta)*np.sinh(kn(n)/lam*y))*np.cos(kn(n)*z)
    top = (beta-beta/np.cosh( kn(n)/lam*gam ) -1.)
    bot = (1-beta*np.tanh( -kn(n)/lam )*np.tanh( kn(n)/lam*gam ) )

    return ( fn(n)*(beta + (top/bot)*( np.cosh( kn(n)*(y/lam) )*( 1+(1-beta)*(bot/top) ) + 
        beta*np.tanh( -kn(n)/lam)*np.sinh( kn(n)*(y/lam) ) )  ) )

   
def u1(y,z):
    return np.sum(u1n(nList, y,z,lam,gam,beta))

def u2(y,z):
    return np.sum(u2n(nList,y,z,lam,gam,beta))

def u(y,z):
    if y > 0:
        return u2(y,z)
    if y<0:
        return u1(y,z)
#Main Program

if __name__ == '__main__':
    nList = np.arange(0,n) #create list of integers from that we will run our sum on.

#Now, act on this array with numpy magic

#just do z = 0 to test this

    etagas = np.linspace(0,gam)
    etaliquid = np.linspace(-1,0)

    zeta = 0 #for test
    
def bc4(n,lam,gam, beta):
    return beta*fn(n)+c3(n,lam,gam,beta)*np.cosh(kn(n)/lam*gam)+c4(n,lam,gam,beta)*np.sinh(kn(n)/lam*gam)



