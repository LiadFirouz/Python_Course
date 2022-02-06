import math

"""Creating a list with all the primes until LIMIT
    using LIST COMPREHENSIONS"""

LIMIT = 100


def main():

    #finding the root of limit for the non primes
    root = int(math.sqrt(LIMIT))

    non_primes = [j
                  for i in range(2, root)
                  for j in range(2 * i, LIMIT, i)]
    primes = [i
              for i in range(LIMIT)
              if not i in non_primes]

    print(primes)


if __name__ == "__main__":
    main()

