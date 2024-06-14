import math

def decisive_vote(n:int)-> float:
    """# The function is calculating the probability of a decisive vote in a population
    # of size `n`. It uses a mathematical formula to determine this probability and returns a
    # decimal number as the result. The formula used in the function is 1 divided by the square
    # root of pi times half of the population size. The function takes an integer `n` as input,
    # representing the population size, and returns the calculated probability as a float.

    Args:
        n (int): [population size]

    Returns:
        float: [decimal number]
    """
    return 1/(math.sqrt(math.pi*(n/2)))

# Percent chance of placing the decisive vote if the population size is 4
print(f'{decisive_vote(4)*100:.4f}%')
# Percent chance of placing the decisive vote if the population size is 10,000,000
print(f'{decisive_vote(10000000)*100:.4f}%')