import random


def getRandomArray(n):
    result = [None]*n

    for i in range(0, len(result)):
        num = random.randint(0, n-1)
        while num in result:
            num = random.randint(0, n-1)
        result[i] = num

    return result


def getSortedArray(n):
    result = [None]*n

    for i in range(0, len(result)):
        result[i] = n-i

    return result


print(getSortedArray(5))