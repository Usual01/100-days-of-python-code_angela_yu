"""
You are painting a wall, The instructions on the paint can says that 1 can paint over 5 square meters
given the random width and height of the wall, calculate cans of paint you'll need to buy
number of cans =(height * width / coverage)
the result should be rounded up
"""
import math
def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    cans = math.ceil(number_of_cans)
    print(f"you will need  {cans} of paint")
test_h = int(input("Height of wall\n"))
test_w = int(input("widht of wall\t"))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)
