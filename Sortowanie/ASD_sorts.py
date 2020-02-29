import random
import math

def bubbleSort(L):
    n = len(L)
    for i in range(n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L



def insertionSort(L):
    n = len(L)
    for i in range(1, n):
        for j in range(i):
            if L[i] <= L[j]:
                L.insert(j, L[i])
                del L[i+1]
                break
    return L


def selectionSort(L):
    n = len(L)
    min = math.inf
    min_i = -1
    for i in range(n):
        for j in range(i,n):
            if min > L[j]:
                min = L[j]
                min_i = j
        L[i],L[min_i] = L[min_i],L[i]
        min = math.inf
    return L

# QUICK_SORT
def partition(L,low,high):
    i=low-1
    pivot = L[high]    # mozna tez inaczej wybrac (np losowo)
    for j in range(low,high):
        if L[j] < pivot:
            i+=1
            L[i],L[j] = L[j],L[i]
    L[i+1],L[high] = L[high],L[i+1]
    return (i+1)

def quickSort(L, low, high):
    if low < high:
        pivot = partition(L,low,high)
        quickSort(L,low,pivot-1)
        quickSort(L,pivot+1,high)
    return L

# MERGE_SORT
def merge(L, left, center, right):
    L2=[]
    i=left
    j=center + 1
    while i <= center and j <= right:
        if L[i] <= L[j]:
            L2.append(L[i])
            i+=1
        if L[i] > L[j]:
            L2.append(L[j])
            j+=1
    while i <= center:
        L2.append(L[i])
        i+=1
    while j <= right:
        L2.append(L[j])
        j+=1
    i=0
    while i <= right-left:  # len(L2) == right - left
        L[left+i] = L2[i]
        i+=1
    return L

def mergeSort(L,start,koniec):
    if start != koniec:
        srodek = (start + koniec)//2
        mergeSort(L, start, srodek)     #rekurencyjne sortowanie lewej czesci tablicy
        mergeSort(L, srodek+1, koniec)  #rekurencyjne sortowanie prawej czesci tablicy
        merge(L, start, srodek, koniec) #operacja scalania kawalkow tablicy podzielonych na 2 posortowane czesci
    return L

def losowe(n):
    L = []
    a = range(0,n)
    for i in range(0,n):
        L.append(random.choice(a))
    return L





n = input("Podaj ilosc danych: ")
L = losowe(int(n))
print(L)

print("\nWpisz numer sortowania, które chcesz przeprowadzić:")
print("1. Bubble sort -- sortowanie babelkowe ")
print("2. Insertion sort -- sortowanie przez wstawianie ")
print("3. Selection sort -- sortowanie przez wybieranie ")
print("4. Quick sort -- sortowanie szybkie ")
print("5. Merge sort -- sortowanie przez scalanie \n")
a=int(input())
if not a in range(1,6):
    print("\nNumer ma byc z zakresu 1-5\n")
    exit()

print("\nPosortowana tablica za pomoca sortowania nr ", str(a),':\n')

if  (a==1):
    print(bubbleSort(L))
elif(a==2):
    print(insertionSort(L))
elif(a==3):
    print(selectionSort(L))
elif(a==4):
    print(quickSort(L,0,int(n)-1))
elif(a==5):
    print(mergeSort(L,0,int(n)-1))
