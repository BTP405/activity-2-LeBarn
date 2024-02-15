def stats_decorator(func):
    def wrapper(numbers):
        #step1: print the numbers read
        print(f"Numbers: {numbers}")

        #step2: print the count of the numbers read
        count = len(numbers)
        print(f"Count: {count}")

        #step3: print the average of the numbers
        average = sum(numbers) / count if count > 0 else 0
        print(f"Average: {average}")

        #step4: print the maximum of the numbers
        maximum = max(numbers) if numbers else None
        print(f"Maximum: {maximum}")

        #call the original function
        return func(numbers)
    return wrapper

def printStats(t, stats_function):
    with open(t, 'r') as file:
        for line in file:
            #convert each line to a list of numbers
            numbers = [float(num) for num in line.strip().split()]

            #call the decorator function
            stats_function(numbers)

#an exaple function to test this code out
@stats_decorator
def custom_stats_function(numbers):
    pass

printStats('numbers_data.txt', custom_stats_function)
