from scipy import optimize
from math import cos,sin
def f(x):
    return cos(x)/(1.+x**2)
x1 = 0.1 #минимальное значение границы поиска
x2 = 2.4 #максимальное значение границы поиска
root_brenth = optimize.brenth (f,x1,x2)
root_bisect = optimize.bisect(f,x1,x2)
root_brentq = optimize.brentq (f,x1,x2)
root_newton_secant = optimize.newton (f,1)
root_newton = optimize.newton (f,1,fprime=lambda x: -2.*x*cos(x)/(x**2+1)**2-sin(x)/(x**2+1.))
print ("Метод Брента 1: x = ", optimize.brenth (f,x1,x2))
print ("Метод деления отрезка: x = ", optimize.bisect(f,x1,x2))
print ("Метод Брента 2: x = ", optimize.brentq (f,x1,x2))
print ("Метод Ньтона (с заданием производной): x = ", optimize.newton (f,1,fprime=lambda x: -2.*x*cos(x)/(x**2+1)**2-sin(x)/(x**2+1.)))
print ("Метод секущих: x = ", optimize.newton (f,1))
get_ipython().run_line_magic('timeit', 'optimize.brenth(f,x1,x2)')
get_ipython().run_line_magic('timeit', 'optimize.bisect(f,x1,x2)')
get_ipython().run_line_magic('timeit', 'optimize.brentq(f,x1,x2)')
get_ipython().run_line_magic('timeit', 'optimize.newton(f,1,fprime=lambda x: -2.*x*cos(x)/(x**2+1)**2-sin(x)/(x**2+1.))')
get_ipython().run_line_magic('timeit', 'optimize.newton (f,1)')
