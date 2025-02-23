import json
from unique import Unique
from print_result import print_result
from field import field
from gen_random import gen_random
from cm_timer import cm_timer_1

path = "C:\\Users\\Vanek\\PycharmProjects\\lab3-4\\data_light.json"

with open(path, encoding="utf-8") as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted([x for x in Unique(field(arg, 'title'), ignore_case = True)])

@print_result
def f2(arg):
    return list(filter(lambda x: x.split()[0] + " программист", arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))

@print_result
def f4(arg):
    return  [f"{employee}, зарплата {salary} руб." for employee, salary in zip(arg, gen_random(len(arg), 100000, 200000))]


if __name__ == "main":
    with cm_timer_1():
        print(f4(f3(f2(f1(data)))))