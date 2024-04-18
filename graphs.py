# Bonch-Bruevich Nikita
# 18/04/24
# This code shows a comparison of the sorting speeds of AdvаncedBubbleSort (blue graph), BubbleSort (green graph), CocktailSort (red graph), GnomeSort(black), ChooseSort(yellow) and InsertSort(brown).

import matplotlib.pyplot as plt
import random as rd
import time as t


def chooseSort(arr):
    N = len(arr)
    for i in range(N):
        min_num = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_num]:
                min_num = j
        if i != min_num:
            arr[i], arr[min_num] = arr[min_num], arr[i]


def gnomeSort(arr):
    N = len(arr)
    index = 0
    while index < N:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1


def insertSort(unsorted):
    N = len(unsorted)
    for i in range(1, N):
        cur = unsorted[i]
        j = i - 1
        while j >= 0 and unsorted[j] > cur:
            unsorted[j + 1] = unsorted[j]
            j -= 1
        unsorted[j + 1] = cur


def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

def advBubbleSort(arr):
    length = len(arr)
    for i in range(length):
        check = 0
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                check += 1
        if check == 0:
            break

def cocktailSort(arr):
    length = len(arr)
    swapped = True
    l = 0
    r = length - 1
    while swapped == True:
        swapped = False
        for i in range(l, r):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if swapped == False:
            break
        swapped = False
        r -= 1
        for i in range(r - 1, l - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        l += 1

count = 0
index = -1
tBubbleSort = [0]*20
tAdvancedBubbleSort = [0]*11
tCocktailSort = [0]*11
tInsertSort = [0]*11
tGnomeSort = [0]*11
tChooseSort = [0]*11
n = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]

for i in range(1000, 12000, 1000):
    index += 1
    for j in range(5):
        t1 = t.time()
        bubbleSort(rd.sample(range(1, 200000), i))
        t2 = t.time()
        count += t2 - t1
    tBubbleSort[index] = (count / 5) ** (1/2)

count = 0
index = -1
for i in range(1000, 12000, 1000):
    index += 1
    for j in range(5):
        t1 = t.time()
        cocktailSort(rd.sample(range(1, 200000), i))
        t2 = t.time()
        count += t2 - t1
    tCocktailSort[index] = (count / 5) ** (1/2)

count = 0
index = -1
for i in range(1000, 12000, 1000):
    index += 1
    for j in range(5):
        t1 = t.time()
        chooseSort(rd.sample(range(1, 200000), i))
        t2 = t.time()
        count += t2 - t1
    tChooseSort[index] = (count / 5) ** (1/2)

count = 0
index = -1
for i in range(1000, 12000, 1000):
    index += 1
    for j in range(5):
        t1 = t.time()
        gnomeSort(rd.sample(range(1, 200000), i))
        t2 = t.time()
        count += t2 - t1
    tGnomeSort[index] = (count / 5) ** (1/2)

count = 0
index = -1
for i in range(1000, 12000, 1000):
    index += 1
    for j in range(5):
        t1 = t.time()
        insertSort(rd.sample(range(1, 200000), i))
        t2 = t.time()
        count += t2 - t1
    tInsertSort[index] = (count / 5) ** (1/2)

plt.plot(n, tBubbleSort, color = 'green')
plt.plot(n, tCocktailSort, color = 'red')
plt.plot(n, tAdvancedBubbleSort, color = 'blue')
plt.plot(n, tChooseSort, color = 'yellow')
plt.plot(n, tInsertSort, color = 'brown')
plt.plot(n, tGnomeSort, color = 'black')
plt.ylabel('Корень времени сортировки')
plt.xlabel('Кол-во элементов массива')
plt.show()