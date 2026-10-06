import numpy as np
import matplotlib.pyplot as plt
import random as rnd
from random import random, randrange
from time import perf_counter, perf_counter_ns

opciones = ["1.Burbuja", "2.Inserción", "3.Selección", "4.Quick Sort", "5.Todos al tiempo"]
print(opciones)
print("Seleccione un algoritmo de ordenamiento:")
seleccion = int(input("Seleccione un algoritmo de ordenamiento (1-5): "))

#Algoritmo de ordenamiento burbuja

if seleccion == 1:

    #Algoritmo de ordenamiento burbuja
    def bubble_sort(A):
        n = len(A)
        for i in range(n - 1):
            for j in range(n - i - 1):
                #operaciones += 1
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
                    #intercambios += 1
            #p+rint(f"paso {i + 1}: {A}")
        return A
        #print(f"Número de operaciones realizadas: {operaciones}.  Número de intercambios: {intercambios}")
    
    
    num_elements = np.arange(1000, 10001, 1000)
    
    size = num_elements.size
    
    #print(size)
    
    #print(num_elements)
    
    t_bubble = np.zeros(size)
    
    for i, n in enumerate(num_elements) :
        vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
        t_inicio = perf_counter_ns()
        bubble_sort(vector_ord)
        t_final = perf_counter_ns()
        t_bubble[i] = t_final - t_inicio
    plt.plot(num_elements, t_bubble, "g-")
    #plt.xlabel("Número de elementos (n)")
    #plt.ylabel("Tiempo (milisegundos)")
    plt.title("Rendimiento de bubble Sort")
    plt.grid(True)
    plt.show()

#Algoritmo de ordenamiento por inserción

if seleccion == 2:
    def insercion_sort(B):
        i = 1
        while i < len(B):
            j = i
            while j > 0 and B[j - 1] > B[j]:
                #operaciones += 1
                B[j], B[j - 1] = B[j - 1], B[j]
                #intercambios += 1
                j -= 1
            i += 1
        #print(f"paso {i + 1}: {B}")
        #prin0t(B)
        return B


    num_elements = np.arange(1000, 10001, 1000)
    size = num_elements.size
    #print(size)
    #print(num_elements)
    t_insertion = np.zeros(size)
    
    
    for i, n in enumerate(num_elements) :
        
        vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
        
        t_inicio = perf_counter_ns()
        
        insercion_sort(vector_ord)
        
        t_final = perf_counter_ns()
        
        t_insertion[i] = t_final - t_inicio
    
    plt.plot(num_elements, t_insertion, "b-")
    #plt.xlabel("Número de elementos (n)")
    #plt.ylabel("Tiempo (milisegundos)")
    plt.title("Rendimiento de Insertion Sort")
    plt.grid(True)
    plt.show()
    
#Algoritmo de ordenamiento por selección

if seleccion == 3:
    def selection_sort(C):
        for i in range(len(C) - 1):
            min = i
            for j in range(i + 1, len(C)):
                #operaciones += 1
                if (C[min] > C[j]):
                    min = j
        if min != i:
            C[min], C[i] = C[i], C[min]
        return C


    num_elements = np.arange(1000, 10001, 1000)

    size = num_elements.size

    #print(size)
    #print(num_elements)
    t_selection = np.zeros(size)
    for i, n in enumerate(num_elements) :
        vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
        t_inicio = perf_counter_ns()
        selection_sort(vector_ord)
        t_final = perf_counter_ns()
        t_selection[i] = t_final - t_inicio
    plt.plot(num_elements, t_selection, "r-")
    plt.show()

#Algoritmo de ordenamiento Quick Sort

if seleccion == 4:
    def quick_sort(D):
        def partition(array, low, high):
            # Mediana de tres para elegir el pivote
            m = (low + high) // 2
            if array[m] < array[low]: 
                array[low], array[m] = array[m], array[low]
            if array[high] < array[low]:
                array[low], array[high] = array[high], array[low]
            if array[m] < array[high]:
                array[m], array[high] = array[high], array[m] 
        
            pivot = array[high]
            i = low - 1
        
            # Reordenamiento de elementos respecto al pivote
            for j in range(low, high):
                if array[j] <= pivot:
                    i += 1
                    array[i], array[j] = array[j], array[i]
                
            array[i + 1], array[high] = array[high], array[i + 1]
            return i + 1

        def quick_sort_rec(array, low, high):
            if low < high:
                pi = partition(array, low, high)
                quick_sort_rec(array, low, pi - 1)
                quick_sort_rec(array, pi + 1, high)

        # Llamada inicial al algoritmo recursivo
        quick_sort_rec(D, 0, len(D) - 1)
        return D

    # Medición e ilustración del tiempo de ejecución
    num_elements = np.arange(1000, 10001, 1000)
    size = num_elements.size
    t_quick_sort = np.zeros(size)

    for i, n in enumerate(num_elements):
        vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
        t_inicio = perf_counter_ns()
        quick_sort(vector_ord)
        t_final = perf_counter_ns()
        t_quick_sort[i] = t_final - t_inicio

    plt.plot(num_elements, t_quick_sort, "-g",)
    plt.title("Complejidad de Quicksort")
    plt.grid(True)
    plt.show()

#Todos los algoritmos al tiempo

if seleccion == 5:
    # Algoritmo de ordenamiento burbuja
    def bubble_sort(A):
        n = len(A)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
        return A

    # Algoritmo de ordenamiento por inserción
    def insercion_sort(B):
        i = 1
        while i < len(B):
            j = i
            while j > 0 and B[j - 1] > B[j]:
                B[j], B[j - 1] = B[j - 1], B[j]
                j -= 1
            i += 1
        return B

    # Algoritmo de ordenamiento por selección
    def selection_sort(C):
        for i in range(len(C) - 1):
            min_idx = i
            for j in range(i + 1, len(C)):
                if C[min_idx] > C[j]:
                    min_idx = j
            if min_idx != i:
                C[min_idx], C[i] = C[i], C[min_idx]
        return C

    # Algoritmo de ordenamiento Quick Sort
    def quick_sort(D):
        def partition(array, low, high):
            m = (low + high) // 2
            if array[m] < array[low]: 
                array[low], array[m] = array[m], array[low]
            if array[high] < array[low]:
                array[low], array[high] = array[high], array[low]
            if array[m] < array[high]:
                array[m], array[high] = array[high], array[m] 
        
            pivot = array[high]
            i = low - 1
        
            for j in range(low, high):
                if array[j] <= pivot:
                    i += 1
                    array[i], array[j] = array[j], array[i]
                
            array[i + 1], array[high] = array[high], array[i + 1]
            return i + 1

        def quick_sort_rec(array, low, high):
            if low < high:
                pi = partition(array, low, high)
                quick_sort_rec(array, low, pi - 1)
                quick_sort_rec(array, pi + 1, high)

        quick_sort_rec(D, 0, len(D) - 1)
        return D

    # Medición e ilustración del tiempo de ejecución
    # Nota: Se usa hasta 2000 elementos para evitar tiempos excesivos en algoritmos O(n^2)
    num_elements = np.arange(200, 2001, 200)
    size = num_elements.size
    t_bubble = np.zeros(size)
    t_selection = np.zeros(size)
    t_insertion = np.zeros(size)
    t_quick_sort = np.zeros(size)

    for i, n in enumerate(num_elements):
        vector_base = np.random.randint(0, 100, n, dtype=np.int16)

        # 1. Bubble Sort
        vector_test = vector_base.copy()
        t_inicio = perf_counter_ns()
        bubble_sort(vector_test)
        t_final = perf_counter_ns()
        t_bubble[i] = t_final - t_inicio

        # 2. Insertion Sort
        vector_test = vector_base.copy()
        t_inicio = perf_counter_ns()
        insercion_sort(vector_test)
        t_final = perf_counter_ns()
        t_insertion[i] = t_final - t_inicio

        # 3. Selection Sort
        vector_test = vector_base.copy()
        t_inicio = perf_counter_ns()
        selection_sort(vector_test)
        t_final = perf_counter_ns()
        t_selection[i] = t_final - t_inicio

        # 4. Quick Sort
        vector_test = vector_base.copy()
        t_inicio = perf_counter_ns()
        quick_sort(vector_test)
        t_final = perf_counter_ns()
        t_quick_sort[i] = t_final - t_inicio

    # Representación gráfica
    plt.plot(num_elements, t_quick_sort, "-y", label="Quick Sort O(n log n)")
    plt.plot(num_elements, t_bubble, "g-", label="Bubble Sort O(n²)")
    plt.plot(num_elements, t_insertion, "b-", label="Insertion Sort O(n²)")
    plt.plot(num_elements, t_selection, "r-", label="Selection Sort O(n²)")
    
    plt.xlabel("Número de elementos (n)")
    plt.ylabel("Tiempo (nanosegundos)")
    plt.title("Comparación de Complejidad de Algoritmos de Ordenamiento")
    plt.legend()
    plt.grid(True)
    plt.show()
