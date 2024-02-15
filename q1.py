def getPrimeNumbers(n):
    #initialize an empty list to store prime numbers
    prime_numbers = []

    #loop through the range from 2 to n 
    for num in range(2, n + 1):
        #first assume the current number is prime
        is_prime = True

        #check for divisors from 2 to the square root of the current number
        for i in range(2, int(num**0.5) + 1):
            #it's not prime if the current number can still be divided by i
            if num % i == 0:
                is_prime = False
                #break out of the inner loop otherwise because no divsor
                break

        #no divisor means the current number is prime
        if is_prime:
            #add the prime number to the list
            prime_numbers.append(num)

    #return the list of prime numbers
    return prime_numbers

#testing example when n is 40
n = 40
prime_numbers = getPrimeNumbers(n)
#final print the prime numbers
print(f"Prime numbers between 2 and {n}: {prime_numbers}")
