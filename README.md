# SalutariDiscreteLogProblemSolver
Python 3 library that uses Agnese Salutari's Algorithm to solve Discrete Logarithm Problems.

## The Problem:
Given a, b and n, find the exponent x that has been used to obtain b starting from a:

  a<sup>x</sup> = b (mod n)
  
where a and b are integers, x is a prime number and n is a prime (n = p) or the product of two prime numbers (n = p1 * p2).

## Salutari's Algorithm:
Salutari's Algorithm solves the problem, step by step, using the following formula:

  b<sub>i</sub> = b<sub>i-1</sub> * a<sup>(-1)</sup> (mod n)

  a<sup>(x - i)</sup> = b<sub>i</sub> (mod n)

where i is an integer that is equal to the number of the current step of the Algorithm.

The Algorithm needs to perform these steps until it reaches the final form, that is the following:

  a<sup>(x - z)</sup> = b<sub>z</sub> = a<sup>y</sup> (mod n)

where y is an integer, z is the last step and b<sub>z</sub> is a perfect power of a.

Then: 

  x = y + z

It works if n is a prime (n = p) and if n is the product of two primes (n = p1 * p2).

### Demonstration: Case 1) n is a prime (n = p):
n is a prime number, so n is coprime with a, then a is invertible (mod n).

  a<sup>x</sup> = b<sub>0</sub> (mod n)

  a<sup>x</sup> - a = b<sub>0</sub> - a (mod n)

  a * (a<sup>(x-1)</sup> - 1) = b<sub>0</sub> - a (mod n)

  a * (a<sup>(x-1)</sup> - 1) * a<sup>(-1)</sup> = (b<sub>0</sub> - a) * a<sup>(-1)</sup> (mod n)

  a<sup>(x-1)</sup> - 1 = b<sub>0</sub> * a<sup>(-1)</sup> - a<sup>0</sup> (mod n)

  a<sup>(x-1)</sup> - 1 + 1 = b<sub>0</sub> * a<sup>(-1)</sup> - 1 + 1 (mod n)

  a<sup>(x-1)</sup> = b<sub>0</sub> * a<sup>(-1)</sup> = b<sub>1</sub> (mod n)

Then: 

  a<sup>(x-1)</sup> = b<sub>1</sub> (mod n) 
    
and so on...

We verify at every step if b<sub>i</sub> is a power of a, until it is true. 

At this z-th step (the last one), we have: 

  a<sup>(x - z)</sup> = b<sub>z</sub> = a<sup>y</sup> (mod n)

Where y is an integer.

Then: 

  x = y + z
  
The final form is always reachable because b is obtained like a power of a (mod n) for definition.


### Demonstration: Case 2) n is the product of two primes (n = p1 * p2) and it's not coprime with a:
  a<sup>x</sup> = b (mod n)
where: 

n = p1 * p2

a = p1 * k, k is an integer.

Then we have: 

  (p1 * k)<sup>x</sup> = b (mod p1 * p2).

So, for the Chinese Remainder Theorem, this can be written as a system of the following two equations:

  (p1 * k)<sup>x</sup> = 0<sup>x</sup> = 0 = b (mod p1)
    
  (p1 * k)<sup>x</sup> = b (mod p2)
    
The first equation is 0 = 0.

We can solve the second equation (mod p2), that is a Case 1) problem, and then find the solution to the original problem
(modulus p1 * p2) with Chinese Remainder Theorem:

  x = x1 + (j * (p1 - 1)) mod (n)
    
 where phi(p1) = p1 - 1 is the Euler Totient Function of the prime number p1.
           
## Contacts

Agnese Salutari – agneses92@hotmail.it

Distributed under the Apache License 2.0. See ``LICENSE`` for more information.

[https://github.com/agnsal](https://github.com/agnsal)


## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
