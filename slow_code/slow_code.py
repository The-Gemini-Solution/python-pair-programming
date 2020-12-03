import random

from time import sleep, time

def long_running_calculation():
    '''
    Models a long running calculation that takes 0.5 seconds to calculate each value and returns 10
    values at once. The values are random integers between 0 and 100.
    '''
    values = []

    for _ in range(10):
        sleep(0.5)
        values.append(random.randint(0, 100))

    return values


def printer(x=3):
    '''
    Prints the first x values from the long running calculations.
    '''
    before = time()

    results = long_running_calculation()

    for i in range(x):
        print(results[i])

    after = time()
    print('elapsed %f s' % (after - before))


def even_printer(x=3):
    '''
    Prints the first x values from the long running calculations.
    '''
    before = time()

    results = long_running_calculation()

    for i in range(x):
        if results[i] % 2 == 0:
            print(results[i])

    after = time()
    print('elapsed %f s' % (after - before))
