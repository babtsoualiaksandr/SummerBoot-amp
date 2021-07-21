#!python3
# -*- coding: utf-8 -*-

"""
The first line of the input file INPUT.TXT contains an integer
N is the height of the palisade according to Old Russian GOSTs.
The second line contains an integer M - the number of stakes needed to build the stockade.
The third line contains
integer H - height of ancient trees of Buyan Island.

Print one number into the output file OUTPUT.TXT - the number of trees that will be given under the ax
"""
try:
    with open('INPUT.TXT', 'r') as f:
        input_values = f.readlines()
    [n, m, h] = [int(x) for x in input_values]
    if not (1 <= n <=  h <= 100):
        raise Exception('1 ≤ N ≤ H ≤ 100')
    if not (1 <= m <= 100):
        raise Exception('1 ≤ M ≤ 100')
except Exception as ex:
    print('Input Error', ex)

result = (m//(h//n)) if (m % (h//n)) == 0 else (m//(h//n)+1)

try:
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))
except Exception as ex:
    print('Output Error', ex)

__author__ = "Aliaksandr Babtsou"
__copyright__ = "Copyright 2021, The Summer Bootcamp"
