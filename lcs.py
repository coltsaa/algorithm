# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:'EiJi'
def lcs(a, b):
    lena = len(a)
    lenb = len(b)
    result = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    flag = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                result[i + 1][j + 1] = result[i][j] + 1
                flag[i + 1][j + 1] = 'ok'
            elif result[i + 1][j] > result[i][j + 1]:
                result[i + 1][j + 1] = result[i + 1][j]
                flag[i + 1][j + 1] = 'left'
            else:
                result[i + 1][j + 1] = result[i][j + 1]
                flag[i + 1][j + 1] = 'up'
    return result, flag


def printLcs(flag, a, i, j):
    if i == 0 or j == 0:
        return
    if flag[i][j] == 'ok':
        printLcs(flag, a, i - 1, j - 1)
        print(a[i - 1], end='')
    elif flag[i][j] == 'left':
        printLcs(flag, a, i, j - 1)
    else:
        printLcs(flag, a, i - 1, j)


a = 'ABCBDAB'
b = 'BDCABA'
result, flag = lcs(a, b)
for i in result:
    print(i)
print('')
for j in flag:
    print(j)
print('')
printLcs(flag, a, len(a), len(b))
print('')
