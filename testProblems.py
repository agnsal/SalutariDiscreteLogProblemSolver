
'''
Copyright 2019 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License
'''

__author__ = 'Agnese Salutari'

# Dependencies:
from SalutariDiscreteLogProblemSolver import DiscreteLogProblemSolver as DLPS
from random import randint
import sympy

'''
    This file is a SalutariDiscreteLogProblemSolver tester and example of usage.
    The problems SalutariDiscreteLogProblemSolver can solve are Discrete Logarithms Problems:
        a^(x) = b (mod n)
        We know a, b and n; we have to find x.
        Salutari's algorithm solve the problem, step by step, using the following formula:
            a^(x - stepsNumber) = b * a^(-1) (mod n)
        It finds x when it reaches the final form, that is the following:
            a^(x - stepsNumber) = a^(y) (mod n)
            => x = y + stepsNumber
        It works if n is a prime (n = p) and if n is the product of two primes (n = p1 * p2).

        If n is the product of two primes (n = p1 * p2):
            a^(x) = b (mod n);   n = p1 * p2 = product pf two prime numbers
                if a = p1 * k, where k is an integer
                then we have: (p1 * k)^(x) = b (mod p1 * p2).
                So, for the Chinese Remainder Theorem, this can be written as a system of the following two equations:
                    (p1 * k)^(x) = 0^(x) = 0 = b (mod p1)
                    (p1 * k)^(x) = b (mod p2)
                The first equation is 0 = 0.
                We can solve the second equation modulus p2 and then find the solution to the original problem
                (modulus p1 * p2) with Chinese Remainder Theorem:
                    x = x1 + (j * (p1 - 1)) mod (n)
'''

print('PROBLEM 1: Book Problem (n is a prime)')
a = 7
b = 12
n = 41
x = 13
print('a = ' + str(a))
print('b = ' + str(b))
print('n = ' + str(n))
solver = DLPS(a=a, b=b, n=n)
solver.printProblemOnFile(problemTitle='Problem 1 (x=' + str(x) + ').', overwrite=True)
solver.solve()
solver.printSolutionsOnFile(problemTitle='Problem 1 (x=' + str(x) + ').', overwrite=True)

print('###################################################################')

print('PROBLEM 2: Toy Problem (n is a prime)')
a = 2
x = 8
n = 11
b = a ** x % n
print('a = ' + str(a))
print('x = ' + str(x))
print('b = ' + str(b))
print('n = ' + str(n))
solver = DLPS(a=a, b=b, n=n)
solver.printProblemOnFile(problemTitle='Problema 2 (x=' + str(x) + ').')
solver.solve()
solver.printSolutionsOnFile(problemTitle='Problema 2 (x=' + str(x) + ').')

print('###################################################################')

print('PROBLEM 3: Random Problem (n is a prime)')
a = sympy.randprime(10, 100)
x = sympy.randprime(10, 100)
n = sympy.randprime(100, 1000)
b = a ** x % n
print('a = ' + str(a))
print('x = ' + str(x))
print('b = ' + str(b))
print('n = ' + str(n))
solver = DLPS(a=a, b=b, n=n)
solver.printProblemOnFile(problemTitle='Problema 3 (x=' + str(x) + ').')
solver.solve()
solver.printSolutionsOnFile(problemTitle='Problema 3 (x=' + str(x) + ').')

print('###################################################################')

print('PROBLEM 4: Random Problem (n is a prime)')
a = sympy.randprime(100, 1000)
x = sympy.randprime(1000, 10000)
n = sympy.randprime(10000, 100000)
b = a ** x % n
print('a = ' + str(a))
print('x = ' + str(x))
print('b = ' + str(b))
print('n = ' + str(n))
solver = DLPS(a=a, b=b, n=n)
solver.printProblemOnFile(problemTitle='Problema 4 (x=' + str(x) + ').')
solver.solve()
solver.printSolutionsOnFile(problemTitle='Problema 4 (x=' + str(x) + ').')

print('###################################################################')

print('PROBLEM 5: Random Problem (n is a prime)')
a = sympy.randprime(10000, 100000)
x = sympy.randprime(100000, 1000000)
n = sympy.randprime(1000000, 10000000)
b = a ** x % n
print('a = ' + str(a))
print('x = ' + str(x))
print('b = ' + str(b))
print('n = ' + str(n))
solver = DLPS(a=a, b=b, n=n)
solver.printProblemOnFile(problemTitle='Problema 5 (x=' + str(x) + ').')
solver.solve()
solver.printSolutionsOnFile(problemTitle='Problema 5 (x=' + str(x) + ').')

print('###################################################################')

print('PROBLEM 6: Random Problem where: n=2*7, a=k*2, k is a random integer')
p1 = 2
p2 = 7
n = p1 * p2
k = randint(1, 1000) % n
a = (k * p1) % n
x = sympy.randprime(1, n)
b = a ** x % n
print('a = ' + str(a))
print('k = ' + str(k))
print('x = ' + str(x))
print('b = ' + str(b))
print('n = ' + str(n))
solver = DLPS(a=a, b=b, n=n)
solver.printProblemOnFile(problemTitle='Problem 6 (x=' + str(x) + ', n=2*7, a=k*2, k is a random integer).')
solver.solve()
solver.printSolutionsOnFile(problemTitle='Problem 6 (x=' + str(solver.getSolutions()) +
                                        ', n=2*7, a=k*2, k is a random integer).')

print('###################################################################')

print('PROBLEM 7: Random Problem with: n=p1*p2, a=k*p1, p1 and p2 are primes, k is a random integer')
p1 = sympy.randprime(100, 1000)
p2 = sympy.randprime(100, 1000)
n = p1 * p2
k = randint(1, 100)
a = k * p1
x = sympy.randprime(1, n)
n = p1 * p2
b = a ** x % n
print('a = ' + str(a))
print('k = ' + str(k))
print('x = ' + str(x))
print('b = ' + str(b))
print('n = ' + str(n) + ' = ' + str(p1) + ' * ' + str(p2))
solver = DLPS(a=a, b=b, n=n)
solver.printProblemOnFile(problemTitle='Problem 7 (x=' + str(x) + ', n=' + str(p1) + '*' + str(p2) +
                                       ', a=k*p1, p1 e p2 primi, k is a random integer).')
solver.solve()
solver.printSolutionsOnFile(problemTitle='Problem 7 (x=' + str(x) + ', n=' + str(p1) + '*' + str(p2) +
                                       ', a=k*p1, p1 e p2 are primes, k is a random integer).')
