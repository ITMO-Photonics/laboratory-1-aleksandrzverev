from scipy import optimize
from math import cos,sin
import time
def f(x):
    return cos(x)/(1.+x**2)

x1 = 0.1 #минимальное значение границы поиска
x2 = 2.4 #максимальное значение границы поиск

start_time = time.time()
root_brenth = optimize.brenth (f,x1,x2)
print("--- %s seconds - time for brenth method" % (time.time() - start_time))
print ("Метод Брента гипер.: x = ", root_brenth)

start_time = time.time()
root_bisect = optimize.bisect(f,x1,x2)
print("--- %s seconds - time for bisect method" % (time.time() - start_time))
print ("Метод деления отрезка: x = ", root_bisect)

start_time = time.time()
root_brentq = optimize.brentq (f,x1,x2)
print("--- %s seconds - time for brentq method" % (time.time() - start_time))
print ("Метод Брента квад.: x = ", root_brentq)

start_time = time.time()
root_newton_secant = optimize.newton (f,1)
print("--- %s seconds - time for secant method" % (time.time() - start_time))
print ("Метод секущих: x = ", root_newton_secant)

start_time = time.time()
root_newton = optimize.newton (f,1,fprime=lambda x: -2.*x*cos(x)/(x**2+1)**2-sin(x)/(x**2+1.))
print("--- %s seconds - time for newton method" % (time.time() - start_time))
print ("Метод Ньтона (с заданием производной): x = ", optimize.newton (f,1,fprime=lambda x: -2.*x*cos(x)/(x**2+1)**2-sin(x)/(x**2+1.)))
