import random
import time

# 1
# e folosit la radixSort
def countingSort(array, exp):

    n = len(array)

    # initializare array de output cu 0 pe toate pozitiile
    output = [0] * (n)

    # initializare array de frecventa cu 0 pe toate pozitiile
    count = [0] * (10)

    # se retine numarul de aparitii in arrayul count
    for i in range(0, n):
        index = array[i] // exp
        count[index % 10] += 1

    # schimbare count[i] astfel incat sa contina pozitia actuala a cifrei
    # respective in arrayul de output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # completare array output
    i = n - 1
    while i >= 0:
        index = array[i] // exp
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    # copiere array output in cel de input pentru a-l putea folosi
    # in functia de radix sort
    i = 0
    for i in range(0, n):
        array[i] = output[i]

def radixSort(array):

    # se cauta maximul pentru a stii numarul maxim de cifre ale unui numar
    maxim = max(array)

    # se face counting sort pentru fiecare cifra a numarului maxim
    exp = 1
    while maxim / exp >= 1:
        countingSort(array, exp)
        exp *= 10

# 2
def mergeSort(array):

    n = len(array)

    if n > 1:
        # se determina mijlocul arrayului
        mid = n // 2
        # se imparte arrayul in 2 jumatati
        left = array[:mid]
        right = array[mid:]
        # se aplica mergeSort pe ambele jumatati
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        # se copiaza data din ambele jumatati in arrayul respectiv
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # se verifica daca a mai ramas vreun element necopiat
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

# 3
def shellSort(array, n):

    gap = n // 2

    while gap > 0:
        j = gap
        # se verifica partea dreapta a arrayului
        while j < n:
            i = j - gap
            while i >= 0:
                # se verifica daca valoarea din dreapta este mai mare
                # daca da, se interschimba, altfel se trece mai departe
                if array[i + gap] > array[i]:
                    break
                else:
                    array[i + gap], array[i] = array[i], array[i + gap]
                #  pentru a se verifica partea stanga a arrayului
                i = i - gap
            j += 1
        gap = gap // 2

# 4
def partition(array, l, r):

    # determinarea pivotului drept mediana din 3
    mid = (l + r)//2
    if array[mid] < array[l]:
        array[mid], array[l] = array[l], array[mid]
    if array[r] < array[l]:
        array[r], array[l] = array[l], array[r]
    if array[mid] < array[r]:
        array[mid], array[r] = array[r], array[mid]
    pivot = array[r]

    # pointer catre element mai mare decat pivotul
    i = l - 1

    # se trece prin tot arrayul, comparand fiecare element cu pivotul
    for j in range(l, r):
        if array[j] <= pivot:
            # daca elementul de pe pozitia j e mai mic decat pivotul, se interschimba
            # cu elementul de pe pozitia i
            i += 1
            array[j], array[i] = array[i], array[j]

    # se interschimba pivotul cu elementul de pe pozitia i
    array[i + 1], array[r] = array[r], array[i + 1]

    # se returneaza pozitia unde s-a facut partitia
    return i + 1

def quickSort(array, l, r):
    if l < r:
        # se gaseste pivotul astfel incat elementele din stanga lui sa fie mai mici decat el
        # iar elementele din dreapta lui sa fie mai mari
        piv = partition(array, l, r)
        # apel recursiv pentru portiunea din stanga pivotului
        quickSort(array, l, piv - 1)
        # apel recursiv pentru portiunea din dreapta pivotului
        quickSort(array, piv + 1, r)

# 5
def bucketSort(array, noOfBuckets):
    # determinare minim si maxim din array
    maxim = max(array)
    minim = min(array)

    # determinare range pentru fiecare bucket
    rang = (maxim - minim) / noOfBuckets

    # creare array temporar
    temp = []

    # creare bucketuri goale
    for i in range(noOfBuckets):
        temp.append([])

    # aranjare elemente in bucketul corect
    for i in range(len(array)):
        diff = (array[i] - minim) / rang - int((array[i] - minim) / rang)
        # elementele ce se afla "pe granita" se duc in bucketul "de mai jos"
        if(diff == 0 and array[i] != minim):
            temp[int((array[i] - minim) / rang) - 1].append(array[i])
        else:
            temp[int((array[i] - minim) / rang)].append(array[i])

    # se sorteaza fiecare bucket
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()

    # se copiaza elementele sortate in arrayul initial
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                array[k] = i
                k += 1

def testSort(array):
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            return False
    return True

def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")

def generateArray(N, max):
    array = [0] * (N)
    for i in range(N):
        array[i] = random.randint(0, max)
    return array

f = open("teste.txt", "r")
tests = int(f.readline())
arrayN = []
arrayMax = []
for line in f:
    l = line.split(" ")
    arrayN.append(int(l[0]))
    arrayMax.append(int(l[1]))

for i in range(tests):
    arr = generateArray(arrayN[i], arrayMax[i])
    print("N = " + str(arrayN[i]) + " Max = " + str(arrayMax[i]) + "\n")
    for j in range(6):
        temp = arr
        startTime = time.time()
        if j == 0:
            radixSort(arr)
            sortName = "Radix Sort"
        if j == 1:
            mergeSort(arr)
            sortName = "Merge Sort"
        if j == 2:
            shellSort(temp, len(temp))
            sortName = "Shell Sort"
        if j == 3:
            quickSort(temp, 0, len(temp) - 1)
            sortName = "Quick Sort"
        if j == 4:
            bucketSort(temp, len(temp))
            sortName = "Bucket Sort"
        if j == 5:
            temp.sort()
            sortName = "Native Sort"
        endTime = time.time()
        print(sortName + ": " + str(endTime - startTime) + "s " + str(testSort(temp)) + "\n")