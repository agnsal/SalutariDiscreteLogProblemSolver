
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
import sympy
import math

class DiscreteLogarithm: # a^(x) = b (mod n)
    '''
    a^(x) = b (mod n)
    phi is the Eulero Totient function of n; this class doesn't calculate it.
    '''
    a = None
    b = None
    n = None
    phi = None
    x = None


    def __init__(self, a=1, b=1, n=1):
        '''
        a^(x) = b (mod n)
        :param a: integer.
        :param b: integer.
        :param n: integer.
        '''
        self.a = a % n
        self.b = b % n
        self.n = n
        self.simplification = 1

    def setA(self, newA=1):
        assert isinstance(newA, int)
        self.a = newA % self.getN()

    def setB(self, newB=1):
        assert isinstance(newB, int)
        self.b = newB % self.getN()

    def setX(self, newX=1):
        assert isinstance(newX, int)
        self.x = newX

    def setN(self, newN=1):
        assert isinstance(newN, int)
        self.n = newN

    def setPhi(self, newPhi=1):
        assert isinstance(newPhi, int)
        self.phi = newPhi

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getX(self):
        return self.x

    def getN(self):
        return self.n

    def getPhi(self):
        return self.phi

class DiscreteLogProblemSolver:
    '''
        a^(x) = b (mod n)
        We know a, b and n; we have to find x.
        Salutari's Algorithm solve the problem, step by step, using the following formula:
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
    originalDL = None # OriginalDL is the initial form of the Discrete Algorithm we need to solve.
    DL = None # DL is the Discrete Logarithm that is changed step by step by the Salutari's Algorithm.
    stepsNumber = None # stepsNumber is the integer representing the steps performed.
    solutions = None # solutions is the list containing all the solutions.

    def __init__(self, a=1, b=1, n=1):
        self.originalDL = DiscreteLogarithm(a=a, b=b, n=n)
        self.DL = DiscreteLogarithm(a=a, b=b, n=n)
        self.stepsNumber = 0
        self.solutions = []

    def setDL(self, a=1, b=1, n=1):
        self.DL = DiscreteLogarithm(a=a, b=b, n=n)

    def setOriginalDL(self, a=1, b=1, n=1):
        self.OriginalDL = DiscreteLogarithm(a=a, b=b, n=n)

    def incrStepsNumber(self):
        self.stepsNumber = self.getStepsNumber() + 1

    def setSolutions(self, newSolutions):
        assert isinstance(newSolutions, list)
        for elem in newSolutions:
            assert isinstance(elem, int)
        self.solutions = newSolutions

    def getDL(self):
        return self.DL

    def getOriginalDL(self):
        return self.originalDL

    def getStepsNumber(self):
        return self.stepsNumber

    def getSolutions(self):
        return self.solutions

    def printDiscreteLogProblem(self):
        print('Find x so that: ' + str(self.getDL().getA()) + '^(x - ' + str(self.getStepsNumber()) + ') = '
              + str(self.getDL().getB())
              + ' (mod ' + str(self.getDL().getN()) + ').')

    def simplify(self):
        '''
        a^(x) = b (mod n);   n = p1 * p2 = product pf two prime numbers
            if a = p1 * k, where k is an integer
            then we have: (p1 * k)^(x) = b (mod p1 * p2).
            So, for the Chinese Remainder Theorem, this can be written as a system of the following two equations:
                (p1 * k)^(x) = 0^(x) = 0 = b (mod p1)
                (p1 * k)^(x) = b (mod p2)
            The first equation is 0 = 0.
            We can solve the second equation modulus p2 and then find the solution to the original problem (
            modulus p1 * p2) with Chinese Remainder Theorem.
                x = x1 + (j * (p1 - 1)) mod (n)
        '''
        a = self.getDL().getA()
        b = self.getDL().getB()
        n = self.getDL().getN()
        gcd = math.gcd(a, n)
        # print('mcd = ' + str(gcd)) # Test
        if not gcd == 1: # If a and n are not coprime
            newN = int(n / gcd)
            # print('newN = ' + str(newN)) # Test
            newA = a % newN
            newB = b % newN
            self.getDL().setN(newN=newN)
            self.getDL().setA(newA=newA)
            self.getDL().setB(newB=newB)
            self.getDL().setN(newN=newN)
            print('a and n are not coprime: for Chinese Remainder Theorem, the problem can be written modulus ' + str(gcd))
        return gcd

    def step(self):
        '''
        Performs a step, that changes DL's b as follows:
            newb = b * a^(-1)
        :return:
        '''
        self.incrStepsNumber()
        print('#### Step: ' + str(self.getStepsNumber()))
        a = self.getDL().getA()
        b = self.getDL().getB()
        n = self.getDL().getN()
        invA = sympy.mod_inverse(a, n)
        print('a^(-1) = ' + str(invA) + ' (mod ' + str(n) + ').')
        newB = b * invA
        self.getDL().setB(newB=newB)

    def isBaPerfectPowerOfA(self, supLimitOrderOfB=10 ** 64):
        '''
        Verifies if b is a power of a, that is:
            b = a^(y).
        :param supLimitOrderOfB: positive number, b as to be less than a * supLimitOrderOfB.
        :return:
        '''
        assert(supLimitOrderOfB > 0)
        # First we try with b not simplified (mod n)
        y = 0
        a = self.getDL().getA()
        p = self.getDL().getB()
        n = self.getDL().getN()
        supLimitOfB = a * supLimitOrderOfB
        if a == 1:
            print('a = 1')  # Test
            return y
        if p == 1:
            print('b = 1')  # Test
            return y
        while p % a == 0:
            y +=1
            p = p / a
            # print('y = ' + str(y)) # Test
            # print('p = ' + str(p)) # Test
        if int(p) == 1:
            print('Final form reached: a^(x - stepsNumber) = a^(y) (mod n).')
            return y
        # Now we try with b simplified (mod n)
        y = 0
        p = self.getDL().getB() % n
        if p == 1:
            self.getDL().setB(newB=p)
            return y
        while p % a == 0:
            y +=1
            p = p / a
            # print('y = ' + str(y)) # Test
            # print('p = ' + str(p)) # Test
        if int(p == 1):
            print('Final form reached: a^(x - stepsNumber) = a^(y) (mod n).')
            if self.getDL().getB() > supLimitOfB:
                self.getDL().setB(newB=self.getDL().getB() % n)
            return y
        return False

    def expandX(self):
        '''
        Finds all the possible solutions (mod n) and writes them in solutions list.
        :return:
        '''
        x = self.getDL().getX()
        newSolutions = [x]
        n = self.getDL().getN()
        originalN = self.getOriginalDL().getN()
        while x + n - 1 < originalN:
            x = x + n - 1  # Here n is a prime -> phi(n) = n - 1
            newSolutions.append(x)
        self.setSolutions(newSolutions=newSolutions)
        print('Solution: x = ' + str(newSolutions) + ' (mod ' + str(n) + ').')

    def computeX(self, y=None):
        '''
        Computes x.
        The final form is:
            a^(x - stepsNumber) = a^(y).
        :param y: integer.
        :return:
        '''
        print('y = ' + str(y))
        solution = y + self.getStepsNumber()
        self.getDL().setX(solution)
        print('x = ' + str(self.getDL().getX()))
        self.expandX()

    def solve(self):
        '''
        Core of the Salutari's Algorithm.
        :return:
        '''
        print('Solving a^(x) = b (mod n) --> a^(x - stepsNumber) = a^(y) (mod n).')
        solved = False
        a = self.getDL().getA()
        if a == 0:
            print('a = 0, 0^(x) = 0 = b for every integer x')
            return
        if a == 1:
            print('a = 1, 1^(x) = 1 = b for every integer x')
            return
        simp = self.simplify()
        if simp:
            self.printDiscreteLogProblem()
        print('phi(n) = ' + str(self.getDL().getPhi()))
        y = self.isBaPerfectPowerOfA()
        if y: # If b is a perfect power of a
            solved = True
        while not solved:
            self.printDiscreteLogProblem()
            self.step()
            self.printDiscreteLogProblem()
            y = self.isBaPerfectPowerOfA()
            if y: # If b is a perfect power of a
                solved = True
        self.computeX(y)

    def verify(self):
        '''
        Verifies if the solutions are true by computing a^(solution) (mod n).
        :return:
        '''
        print('Verify')
        a = self.getOriginalDL().getA()
        ver = []
        if a == 0:
            print('0^(x) = 0 for every x.')
            ver.append(0)
        elif a == 1:
            print('1^(x) = 1 for every x.')
            ver.append(1)
        else:
            n = self.getOriginalDL().getN()
            sol = self.getSolutions()
            for s in sol:
                v = a ** s % n
                print(str(a) + '^(' + str(s) + ') = ' + str(v) + ' (mod ' + str(n) + ').')
                ver.append(v)
        return ver

    def printProblemOnFile(self, filePath='DLproblem.txt', problemTitle='Problem', overwrite=False):
        '''
        Prints problem on a file.
        :param filePath: string.
        :param problemTitle: string.
        :param overwrite: boolean.
        :return:
        '''
        if overwrite:
            file = open(filePath, 'w')
        else:
            file = open(filePath, 'a')
        file.write('#####################' + str(problemTitle) + '\n')
        file.write('a^(x) = b (mod n);  x=? \n')
        file.write('a = ' + str(self.getDL().getA()) + '\n')
        file.write('x = ' + str(self.getSolutions()) + '\n')
        file.write('b = ' + str(self.getDL().getB()) + '\n')
        file.write('n = ' + str(self.getDL().getN()) + '\n')
        file.close()

    def printSolutionsOnFile(self, filePath='DLsolution.txt', problemTitle='Problem', overwrite=False):
        '''
        Prints solutions on a file.
        :param filePath: string.
        :param problemTitle: string.
        :param overwrite: boolean.
        :return:
        '''
        sol = self.getSolutions()
        a = self.getOriginalDL().getA()
        b = self.getOriginalDL().getB()
        n = self.getOriginalDL().getN()
        ver = self.verify()
        if overwrite:
            file = open(filePath, 'w')
        else:
            file = open(filePath, 'a')
        file.write('#### Solution to problem ' + str(problemTitle) + ':\n')
        file.write('Solutions = ' + str(sol) + '\n')
        file.close()
        file = open(filePath, 'a')
        file.write(str(a) + '^(' + str(sol) + ') = ' + str(ver) + ' = b = ' + str(b) + ' (mod ' + str(n) + ').\n')
        file.close()
