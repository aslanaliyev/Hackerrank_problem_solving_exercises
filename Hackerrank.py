# Aslan Aliyev 

# #
# def simpleArraySum(ar):
#     #
#     # Write your code here.
#     #
#     n = len(ar)
#     sum = 0
#     print(n)
#     for i in range(0,n):
#         a = ar[i]
#         sum = sum + a
#
#     return print(sum)
#
# a = [10000000,10000015,10000025]
#
# simpleArraySum(a)
#
#
# def plusMinus(arr):
#     length = len(arr)
#     pos = 0
#     neg = 0
#     zero = 0
#     for i in range(length):
#         if arr[i] > 0:
#            pos += 1
#         elif arr[i] < 0:
#             neg += 1
#         else:
#             zero += 1
#     print(length)
#     positive = pos / length
#     negative = neg / length
#     zero1 = zero / length
#
#     return positive, negative, zero1
# a = [-8,77,0,6,5,5,5,8,5,0]
# print(plusMinus(a))

#
# def staircase(n):
#     for i in range(1, n+1): print(str('#' * i).rjust(4))
#
#
# staircase(4)
#
# def miniMaxSum(arr):
#     arr.sort()
#     length = len(arr) - 1
#     length1 = len(arr)
#     min = 0
#     max = 0
#     for i in range(length):
#         min += arr[i]
#     for j in reversed(range(1,length1)):
#         max += arr[-j]
#     print(min, max)
#
#
# d = [1,2,3,4,5]
#
# miniMaxSum(d)
#

#
# def timeConversion(s):
#     #
#     # Write your code here.
#     #
#     if s[8:10] == "PM":
#         hour = int(s[:2]) + 12
#         hour = str(hour)
#         s = s.replace(s[:2], hour)
#         s = s.replace(s[8:10], "")
#     else:
#         s = s.replace(s[8:10], "")
#     print(s)
#
#
# a = "07:05:45AM"
# timeConversion(a)

import math
import os
import random
import re
import sys
#
#
# def gradingStudents(grades):
#     for i in range(len(grades)):
#         if grades[i] <= 37:
#             grades[i] = grades[i]
#         elif ((grades[i] / 5) - int(grades[i]/5)) > 0.5:
#             grades[i] = round(grades[i]/5)*5
#         elif ((grades[i] / 5) - int(grades[i]/5)) < 0.5:
#             grades[i] = grades[i]
#     return grades
#
#
# a = [73,67,38, 33]
#
# gradingStudents(a)
#
#
# def kangaroo(x1, v1, x2, v2):
#     for i in range(0, 10000):
#         x1 += v1
#         x2 += v2
#         if x1 == x2:
#             a = "YES"
#
#     return a
#
#
#
# kangaroo(0,3,4,2)
#
# import operator
# def migratoryBirds(arr):
#     index = []
#     number = []
#     for i, x in enumerate(arr):
#         index.append(i)
#         number.append(arr.count(arr[i]))
#     dictionary = dict(zip(index, number))
#     answer = max(dictionary.items(), key=operator.itemgetter(1))[0]
#     #u = dictionary.get(answer)
#     return print(arr[answer])

#
# def migratoryBirds(arr):
#     bird_freq = [0, 0, 0, 0, 0, 0]
#     for i in range(len(arr)):
#         bird_freq[arr[i]] += 1
#     return bird_freq.index(max(bird_freq))
#
# #migratoryBirds(c)
#
#
# def birthdayCakeCandles(ar):
#     max_number = max(ar)
#     count = 0
#     for i in ar:
#         if max_number == i:
#             count += 1
#     return print(count)
#
#
#
#
#
#
# c = [1,2,3,4,4]
#
# birthdayCakeCandles(c)
#
#
# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     apple_count = 0
#     orange_count = 0
#     for i in apples:
#         if i > 0:
#             if (a + i) >= s and (a + i) <= t:
#                 apple_count += 1
#
#     for j in oranges:
#         if j < 0:
#             if (b + j) >= s and (b + j) <= t:
#                 orange_count += 1
#     return print(apple_count, orange_count)
#
#
# countApplesAndOranges(7, 11, 5, 15, [-2,2,1], [5,-6])
#
# import collections
# def sockMerchant(n, ar):
#     countz = collections.Counter(ar)
#     print(countz)
#     answer = 0
#     for i in countz.values():
#         if i == 1:
#             pass
#         elif i % 2 == 0:
#             answer += i/2
#         else:
#             answer += (i-1)/2
#     return print(int(answer))
#
#
#
#
# sockMerchant(6, [10,20,20,10,10,30,50,10,20])
import numpy as np
#
# def pageCount(n,p):
#     page_flip = (p-1)/2 + 0.5
#     if n % 2 == 0:
#         if (n - p) % 2 != 0:
#             page_flip_reverse = (n - p)/2 + 0.5
#         else:
#             page_flip_reverse = (n - p) // 2
#     else:
#         if (n - p) % 2 != 0:
#             page_flip_reverse = (n - p) / 2 + 0.5 - 1
#         else:
#             page_flip_reverse = (n - p) // 2
#
#     #page_flip_reverse = (n - p)%2
#     return min(int(page_flip),int(page_flip_reverse))

#
# pageCount(8,6)
#
# number_of_cases = int(input())
#
# def letter_switcher(word):
#     first = ""
#     second = ""
#     for i in range(0, len(word)):
#         if i == 0 or i % 2 == 0:
#             first += word[i]
#         else:
#             second += word[i]
#         final = first + " " + second
#     print(final)
#
# for j in range(number_of_cases):
#     letter_switcher(input())
#
# def catAndMouse(x, y, z):
#     if abs(z-x) == abs(z-y):
#         print("Mouse C")
#     elif abs(z-x) > abs(z-y):
#         print("Cat B")
#     elif abs(z-x) < abs(z-y):
#         print("Cat A")
#
#
# catAndMouse(1, 3, 2)

#
# def findDigits(n):
#     numbers = [int(d) for d in str(n)]
#     count = 0
#     for i in numbers:
#         if i == 0:
#             pass
#         elif n % i == 0:
#             count += 1
#     return print(count)
#
#
# findDigits(330)
#

#
# def extraLongFactorials(n):
#     factorial = 1
#     for i in range(n, 1,-1):
#         factorial = factorial * i
#     return print(factorial)
#
# extraLongFactorials(25)
# for i in range(0,10):
#     print(i)


#
# def pickingNumbers(a):
#     # Write your code here
#     for j in a:
#         for i in a:
#             if i == j:
#                 print(a.index(j))
#
#
# pickingNumbers([1,2,2,3,3,4,4,5,5,1,8])


#
#
# def getTotalX(a, b):
#     # Write your code here
#     count = 0
#     for i in range(a[0],b[0]):
#         for j in a:
#             if i % j == 0:
#                 count +=1
#             else:
#                 count -= 1
#     return print(count)
#
#
# getTotalX([2,3],[9,13])
#
#
#
# phoneBook = {"sam":"99912222","dsf":"fsf"}
#
# print(phoneBook.key()[0])

#
# n = int(input())
#
# dict = {}
#
# for i in range(n):
#     split_str = input().split()
#     dict[split_str[0]] = split_str[1]
#
#
# for j in range(n):
#     input_index = str(input())
#     if input_index in dict:
#         print("%s=%s" % (input_index,dict[input_index]))
#     else:
#         print("Not found")


#
# def howManyGames(p, d, m, s):
#     # Return the number of games you can buy
#     n = 0
#     total_money = s
#     limit = m
#     game_cost = p
#     deduct = d
#     for _ in range(500):
#         if total_money > game_cost:
#             if game_cost >= limit:
#                total_money = total_money - game_cost
#                game_cost = game_cost - deduct
#                n += 1
#
#         else:
#             break
#
#
#     return print(n,game_cost)
#
#
# howManyGames(20,3,6,65000)

#
# def birthday(s, d, m):
#     result = []
#     count = 0
#     for i in range(0, len(s),1):
#         result.append(s[i:i + m])
#         print(i)
#     for k in result:
#         if d == sum(k):
#             count +=1
#
#     return print(count,result)
#
#
#
#
# birthday([5,5,4,6,9,6,2,4], 10, 2)
#
import functools

#
# def getTotalX(a, b):
#     import sys
#     from functools import reduce
#     from fractions import gcd
#
#     lcm_a = reduce(lambda x, y: x * y // gcd(x, y), a)
#     gcd_b = reduce(gcd, b)
#     print(sum(1 for x in range(lcm_a, gcd_b + 1, lcm_a) if gcd_b % x == 0))
#
# getTotalX((2,4), (16,32,64))

#
# def countingValleys(n, s):
#     start = 0
#     valley = 0
#     for i in s:
#         if start==0 and i=="D":
#             valley +=1
#         if i == "D":
#             start -= 1
#         else:
#             start += 1
#
#     print (valley)
#
# countingValleys(8, ("UDDDUDUU"))

# print(ord("a"))

#
# def bigSorting(unsorted):
#     for i in sorted(unsorted):
#         print(i)
#
#
# bigSorting((2,1,3))

#
# def circularArrayRotation(a, k, queries):
#     answer = []
#     for z,i in enumerate(queries):
#         if k > len(a):
#             k = len(a) % k
#         if k < i:
#             answer.append(a[i-k])
#         elif k > i:
#             answer.append(a[len(a) - k + i])
#         print(answer[z])
#
#
#
#
#
# circularArrayRotation((1, 2, 3), 10, (0,1))
#
# a = ((1, 2, 3), (12, 3, 4))

# print(min(a[0]))
#
# n = (2,3,1,2,3,2,3,3)
# cases = ((0,3,5),(4,6))


#
# def serviceLane(n, cases):
#     answer = []
#     for i in cases:
#         minimum = i[0]
#         maximum = i[1]
#         answer.append(min(n[minimum:maximum+1]))
#     print(answer)
#     for z in answer:
#         return print(z)
#
# serviceLane(n, cases)

#
# def serviceLane(n, cases):
#     return [min(width[x:y+1]) for x,y in cases]
#
#
# z = [x+y for x,y in cases]
# print(z)


p = (4, 3, 5, 1, 2)


# print(p.index(1)+1)
#
# def permutationEquation(p):
#     answer = []
#     for z in range(1, len(p) + 1):
#         answer.append([i + 1 for i, e in enumerate(p) if e == z])
#     answer1 = []
#     for k in range(0, len(answer)):
#         answer1.append(answer[k][0])
#     new = []
#     for z in answer1:
#         new.append([i + 1 for i, e in enumerate(p) if e == z])
#     last = []
#     for m in range(0, len(answer)):
#         last.append(new[m][0])
#     return last
#
# def permutationEquation(p):
#     per=[]
#     for i in range(len(p)):
#         per.append(p.index(p.index(i+1)+1)+1)
#     return print(per)
#
# permutationEquation(p)
# from collections import Counter
#
# arr = (3, 3, 2, 1, 3)
# arr1 = (1, 2, 3, 1, 2, 3, 3, 3)
# def equalizeArray(arree):
#     d = Counter(arree).values()
#     print(d)
#     deletion = len(arree) - max(d)
#
#
# def equalizeArray(arree):
#     count = [arr.count(i) for i in aree]
#
#
# equalizeArray(arr1)
#
#
# def fairRations(B):
#     count = 0
#     B = list(B)
#     if B[0] % 2 != 0:
#         B[0] = B[0] + 1
#         B[1] = B[1] + 1
#         count = 2
#     for i in range(1,len(B) - 1):
#         if B[i] % 2 != 0:
#             B[i] = B[i] + 1
#             B[i+1] = B[i+1] + 1
#             count = count + 2
#     if B[len(B)-1] % 2 != 0:
#         return "NO"
#     else:
#         return (count)
#
#
#
# B = (1, 2)
#
# fairRations(B)



#
# def beautifulTriplets(d, arr):
#     answer_list = []
#     for j in range(0,len(arr)-1):
#         for i in range(1,len(arr)):
#             if arr[i] - arr[j] == d :
#                 answer_list.append(arr[j])
#                 answer_list.append(arr[i])
#
#
#
#
#     print(answer_list)
#
#
#
#
# arr = (1, 2, 4, 5, 7, 8, 10)
# d = 3
#
# beautifulTriplets(d, arr)

#
# def beautifulTriplets(d, arr):
#     answer_list = []
#     count = 0
#     for i in arr:
#         if i + 3 in arr:
#             first_number = i
#             second_number = i + 3
#             if second_number + 3 in arr:
#                 third_number = second_number + 3
#                 answer_list.append(first_number)
#                 answer_list.append(second_number)
#                 answer_list.append(third_number)
#                 count += 1
#
#
#
#     print(count)
#
#
#
# arr = (1, 2, 4, 5, 7, 8, 10)
# d = 3
#
# beautifulTriplets(d, arr)

#
#
# def beautifulTriplets(d, arr):
#     answer_list = []
#     count = 0
#     for i in arr:
#         if (i + d and i + d*2) in arr:
#             count += 1
#
#
#
#
#     print(count)
#
#
#
# arr = (1, 2, 4, 5, 7, 8, 10)
# d = 3
#
# beautifulTriplets(d, arr)
#
#
# def jumpingOnClouds(c, k):
#     energy = 100
#     index_of_1 = [ind for ind,val in enumerate(c) if val==1]
#     print(index_of_1)
#     for i in range(0,len(c)+1,k):
#         print(i)
#         energy -= 1
#         if i in index_of_1:
#             energy -= 2
#
#     print(energy)
#
#
# c = (1, 1, 1, 0, 1, 1, 0, 0, 0, 0)
#
# k = 3
#
# jumpingOnClouds(c, k)
#
#
# def jumpingOnClouds(c):
#     c = [index for index, value in enumerate(c) if value == 0]
#     diff = []
#     print(c)
#     for i in range(len(c)-1):
#         diff.append(c[i+1] - c[i])
#     print(diff)
#
#
# c = (0, 0, 1, 0, 0, 1, 0)
# jumpingOnClouds(c)

from collections import Counter

def appendAndDelete(s, t):
    dict_s = {}
    dict_t = {}
    n = 0
    for i in sorted(s):
        dict_s.update({i : s.count(i)})
    for j in sorted(t):
        dict_t.update({j : t.count(j)})
    dict_s = Counter(dict_s)
    dict_t = Counter(dict_t)
    diff = dict_t-dict_s

    print(dict_s)
    print(dict_t)
    print(diff)





s = "hackerhappy"
t = "hackerrank"
appendAndDelete(s, t)
