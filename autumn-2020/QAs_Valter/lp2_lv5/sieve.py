""" The Sieve of Eratosthenes is an elegant algorithm for finding all of
the
prime numbers up to some limit n. The basic idea is to first create a list
of numbers from 2 to n. The first number is removed from the list, and
announced as a prime number, and all multiples of this number up to n
are removed from the list. This process continues until the list is empty.

Write a program that prompts a user for n and then uses the sieve
algorithm to find all the primes less than or equal to n . """


def sieve(n):
    nums = list(range(2, n + 1))
    primes = []
    while nums:
        prime = nums.pop(0)
        primes.append(prime)
        for num in nums:
            if num % prime == 0:
                nums.remove(num)
    return primes


def main():
    n = int(input("n: "))
    print(sieve(n))


if __name__ == "__main__":
    main()
