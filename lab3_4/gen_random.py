import random

def gen_random(num_count, begin, end):
    list = [int(random.uniform(begin, end)) for i in range(num_count)]
    return list
if __name__ =='__main__':
    print(*gen_random(5, 1, 3))
