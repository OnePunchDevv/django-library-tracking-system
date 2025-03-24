import random
# rand_list =

def rand_list():
    rand_nums = [random.randint(1, 20) for _ in range(10)]
    return rand_nums

# list_comprehension_below_10 =
def list_comprehension_below_10(rand_nums):
    return [ num for num in rand_nums if num < 10]

# list_comprehension_below_10 =
def list_comprehension_below_10(rand_nums):
    return list(filter(lambda num: num < 10, rand_nums))