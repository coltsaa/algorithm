# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:'EiJi'
import time
array = [1, 2, -4, 3, 4, 6, -6, 7, 14, -14, 15, -15, 28, -28, 36, -36, 54, -54]

# 动态规划

def maxSumOnDp(array):
    lena = len(array)
    sum = 0
    start = 0
    for i in range(0, lena):
        if start > 0:
            start = start + array[i]
        else:
            start = array[i]
        if start > sum:
            sum = start
    return sum

if __name__=='__main__':
    start = time.clock()
    res = maxSumOnDp(array)
    end = time.clock()
    print('动态规划:')
    print('the max sub sum is %d' % res)
    print("read: %f s" % (end - start))

# 分治

def maxSubSumOnDc(array, left, right):

    if left == right:
        if array[left] > 0:
            sums = array[left]
        else:
            sums =  0
    else:
        center = (left + right)//2
        leftSum = maxSubSumOnDc(array, left, center)
        rightSum = maxSubSumOnDc(array, center+1, right)
        lefts = 0
        s1 = 0
        for i in range(center-1, left-1, -1):
            lefts += array[i]
            if lefts > s1:
                s1 = lefts
        rights = 0
        s2 = 0
        for i in range(center, right+1):
            rights = rights + array[i]
            if rights > s2:
                s2 = rights
        sums = s1 + s2
        if sums < leftSum:
            return leftSum
        if sums < rightSum:
            return rightSum
    return sums

if __name__=='__main__':
    lenb = len(array)-1
    start = time.clock()
    res = maxSubSumOnDc(array,0,lenb)
    end = time.clock()
    print('分治:')
    print('the max sub sum is %d' % res)
    print("read: %f s" % (end - start))

# 暴力

def maxSubSumOnViolence(array):
    maxSum = 0
    sum = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            sum = array[i]
            array[i] += array[j]
            if array[i]>sum:
                sum = array[i]
        if sum>maxSum:
            maxSum = sum
    return maxSum

if __name__=='__main__':
    start = time.clock()
    res = maxSubSumOnViolence(array)
    end = time.clock()
    print('暴力:')
    print('the max sub sum is %d' % res)
    print("read: %f s" % (end - start))
