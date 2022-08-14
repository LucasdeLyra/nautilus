
#Questão 1
import re


def first_equals_last(numberslist):
    return numberslist[0] == numberslist[-1]

#Questão 2
def erastothenes_sieve(num):
    primes = [True] * (num+1)
    for i in range(2, int(num**(1/2))+1):
        if primes[i] == True:
            for j in range(i**2, num+1, i):
                primes[j] = False
    return [i for i, boolean in enumerate(primes) if boolean][2:]


def last_prime_divisor(num):
    primes = erastothenes_sieve(num)
    for i in range(len(primes)-1, 1, -1):
        if num%primes[i]==0:
            return primes[i]

#Questão 3
def palindrome(num):
    strnum = str(num)
    for i in range(len(strnum)//2):
        if strnum[i] != strnum[len(strnum)-1-i]:
            return False
    return True

#Questão 4
def sum_primes(num=1000):
    return sum(erastothenes_sieve(num))
print(sum_primes())
