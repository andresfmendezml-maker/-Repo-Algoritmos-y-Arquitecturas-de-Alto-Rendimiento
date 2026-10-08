import numpy as np
import matplotlib.pyplot as plt
import random as rnd
from random import random, randrange
from time import perf_counter, perf_counter_ns

opciones = [
    "1.Burbuja", 
    "2.Inserción", 
    "3.Selección", 
    "4.Quick Sort", 
    "5.Merge Sort", 
    "6.Todos los algoritmos al tiempo", 
    "7.G1: O(n^2) lineal", 
    "8.G2: Quicksort y Avanzado lineal", 
    "9.G3: Escala Log-Log", 
    "10.G4: Tiempos Normalizados", 
    "11.G5: Casos de Entrada (Aleatorio, Ordenado, Inverso)", 
    "12.G6: Quicksort con Rangos (0-99 vs 0-10^6)"
]

for op in opciones:
    print(op)

seleccion = int(input("Seleccione la opcion que desee (1-12): "))

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

#Algoritmo de ordemiento Merge Sort

if seleccion == 5:
    def merge_sort(E):
        if len(E) > 1:
            mid = len(E) // 2
            
            # Dividir el arreglo en dos mitades
            L = E[:mid]
            R = E[mid:]
            
            # Llamadas recursivas para ordenar cada mitad
            merge_sort(L)
            merge_sort(R)
            
            i = j = k = 0
            
            # Mezclar las dos mitades ordenadas
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    E[k] = L[i]
                    i += 1
                else:
                    E[k] = R[j]
                    j += 1
                k += 1
                
            # Verificar si quedaron elementos en L
            while i < len(L):
                E[k] = L[i]
                i += 1
                k += 1
                
            # Verificar si quedaron elementos en R
            while j < len(R):
                E[k] = R[j]
                j += 1
                k += 1

    num_elements = np.arange(1000, 100001, 1000)
    size = num_elements.size
    #print(num_elements)

    t_merge = np.zeros(size)

    for i, n in enumerate(num_elements):
        vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
        t_inicio = perf_counter_ns()
        merge_sort(vector_ord)
        t_final = perf_counter_ns()
        t_merge[i] = t_final - t_inicio

    plt.plot(num_elements, t_merge, "g-")
    plt.xlabel("Número de elementos")
    plt.ylabel("Tiempo (nanosegundos)")
    plt.title("Rendimiento de Merge Sort")
    plt.show()

#Todos los algoritmos al tiempo

if seleccion == 6:
    
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

    # Algoritmo de ordenamiento Merge Sort
    def merge_sort(E):
        if len(E) <= 1:
            return E
        mid = len(E) // 2
        left = merge_sort(E[:mid])
        right = merge_sort(E[mid:])
        
        result = np.empty(len(E), dtype=E.dtype)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result[k] = left[i]
                i += 1
            else:
                result[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            result[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            result[k] = right[j]
            j += 1
            k += 1
            
        return result

    # Medición e ilustración del tiempo de ejecución
    # Nota: Se usa hasta 2000 elementos para evitar tiempos excesivos en algoritmos O(n^2)
    num_elements = np.arange(5, 201, 1)
    size = num_elements.size
    t_bubble = np.zeros(size)
    t_selection = np.zeros(size)
    t_insertion = np.zeros(size)
    t_quick_sort = np.zeros(size)
    t_merge_sort = np.zeros(size)

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

        # 5. Merge Sort
        vector_test = vector_base.copy()
        t_inicio = perf_counter_ns()
        merge_sort(vector_test)
        t_final = perf_counter_ns()
        t_merge_sort[i] = t_final - t_inicio

    # Representación gráfica
    plt.plot(num_elements, t_quick_sort, "-y", label="Quick Sort O(n log n)")
    plt.plot(num_elements, t_merge_sort, "-m", label="Merge Sort O(n log n)")
    plt.plot(num_elements, t_bubble, "g-", label="Bubble Sort O(n²)")
    plt.plot(num_elements, t_insertion, "b-", label="Insertion Sort O(n²)")
    plt.plot(num_elements, t_selection, "r-", label="Selection Sort O(n²)")
    
    plt.xlabel("Número de elementos (n)")
    plt.ylabel("Tiempo (nanosegundos)")
    plt.title("Comparación de Complejidad de Algoritmos de Ordenamiento")
    plt.legend()
    plt.grid(True)
    plt.show()

#G1: Comparación de algoritmos de ordenamiento O(n²)

if seleccion == 7:
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

    num_elements = np.arange(200, 2001, 200)
    size = num_elements.size
    t_bubble = np.zeros(size)
    t_selection = np.zeros(size)
    t_insertion = np.zeros(size)
    

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
    
    # Representación gráfica
    plt.plot(num_elements, t_bubble, "g-", label="Bubble Sort O(n²)")
    plt.plot(num_elements, t_insertion, "b-", label="Insertion Sort O(n²)")
    plt.plot(num_elements, t_selection, "r-", label="Selection Sort O(n²)")
        
    plt.xlabel("Número de elementos (n)")
    plt.ylabel("Tiempo (nanosegundos)")
    plt.title("Comparación de Complejidad de Algoritmos de Ordenamiento")
    plt.legend()
    plt.grid(True)
    plt.show()
    
#G2: Comparación de algoritmos de ordenamiento O(n log2 n)

if seleccion == 8:
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
    
    # Algoritmo de ordenamiento Merge Sort
    def merge_sort(E):
        if len(E) <= 1:
            return E
        mid = len(E) // 2
        left = merge_sort(E[:mid])
        right = merge_sort(E[mid:])
            
        result = np.empty(len(E), dtype=E.dtype)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result[k] = left[i]
                i += 1
            else:
                result[k] = right[j]
                j += 1
            k += 1
                
        while i < len(left):
            result[k] = left[i]
            i += 1
            k += 1
                
        while j < len(right):
            result[k] = right[j]
            j += 1
            k += 1
                
        return result
    
    # Medición e ilustración del tiempo de ejecución
    # Nota: Se usa hasta 2000 elementos para evitar tiempos excesivos en algoritmos O(n^2)
    num_elements = np.arange(250, 2001,250)
    size = num_elements.size
    t_quick_sort = np.zeros(size)
    t_merge_sort = np.zeros(size)
    
    for i, n in enumerate(num_elements):
        
        vector_base = np.random.randint(0, 100, n, dtype=np.int16)
        
        #Quick Sort
        vector_test = vector_base.copy()
        t_inicio = perf_counter_ns()
        quick_sort(vector_test)
        t_final = perf_counter_ns()
        t_quick_sort[i] = t_final - t_inicio
        
        #Merge Sort
        vector_test = vector_base.copy()
        t_inicio = perf_counter_ns()
        merge_sort(vector_test)
        t_final = perf_counter_ns()
        t_merge_sort[i] = t_final - t_inicio
        
    # Representación gráfica
    plt.plot(num_elements, t_quick_sort, "-y", label="Quick Sort O(n log n)")
    plt.plot(num_elements, t_merge_sort, "-m", label="Merge Sort O(n log n)")
        
    plt.xlabel("Número de elementos (n)")
    plt.ylabel("Tiempo (nanosegundos)")
    plt.title("Comparación de Complejidad de Algoritmos de Ordenamiento")
    plt.legend()
    plt.grid(True)
    plt.show()
    
#G3: Comparación de algoritmos de ordenamiento O(n log n) y O(n²) con ajuste lineal en escala log-log

if seleccion == 9:
    
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

    # Algoritmo de ordenamiento Merge Sort
    def merge_sort(E):
        if len(E) <= 1:
            return E
        mid = len(E) // 2
        left = merge_sort(E[:mid])
        right = merge_sort(E[mid:])
        
        result = np.empty(len(E), dtype=E.dtype)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result[k] = left[i]
                i += 1
            else:
                result[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            result[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            result[k] = right[j]
            j += 1
            k += 1
            
        return result

    # Medición e ilustración del tiempo de ejecución
    num_elements = np.arange(200, 2001, 200)
    size = num_elements.size
    t_bubble = np.zeros(size)
    t_selection = np.zeros(size)
    t_insertion = np.zeros(size)
    t_quick_sort = np.zeros(size)
    t_merge_sort = np.zeros(size)

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

        # 5. Merge Sort
        vector_test = vector_base.copy()
        t_inicio = perf_counter_ns()
        merge_sort(vector_test)
        t_final = perf_counter_ns()
        t_merge_sort[i] = t_final - t_inicio

    # Ajuste lineal en escala logarítmica: log(t) = m * log(n) + c  =>  t = exp(c) * n^m
    log_n = np.log(num_elements)

    def fit_log_log(t_arr):
        log_t = np.log(t_arr)
        m, c = np.polyfit(log_n, log_t, 1)
        return m, np.exp(c)

    m_quick, a_quick = fit_log_log(t_quick_sort)
    m_merge, a_merge = fit_log_log(t_merge_sort)
    m_bubble, a_bubble = fit_log_log(t_bubble)
    m_insertion, a_insertion = fit_log_log(t_insertion)
    m_selection, a_selection = fit_log_log(t_selection)

    # Representación gráfica en escala log-log con rectas de ajuste
    plt.loglog(num_elements, t_quick_sort, "yo", label="Quick Sort (datos)")
    plt.loglog(num_elements, a_quick * (num_elements ** m_quick), "y--", label=f"Ajuste Quick Sort (m={m_quick:.2f})")

    plt.loglog(num_elements, t_merge_sort, "mo", label="Merge Sort (datos)")
    plt.loglog(num_elements, a_merge * (num_elements ** m_merge), "m--", label=f"Ajuste Merge Sort (m={m_merge:.2f})")

    plt.loglog(num_elements, t_bubble, "go", label="Bubble Sort (datos)")
    plt.loglog(num_elements, a_bubble * (num_elements ** m_bubble), "g--", label=f"Ajuste Bubble Sort (m={m_bubble:.2f})")

    plt.loglog(num_elements, t_insertion, "bo", label="Insertion Sort (datos)")
    plt.loglog(num_elements, a_insertion * (num_elements ** m_insertion), "b--", label=f"Ajuste Insertion Sort (m={m_insertion:.2f})")

    plt.loglog(num_elements, t_selection, "ro", label="Selection Sort (datos)")
    plt.loglog(num_elements, a_selection * (num_elements ** m_selection), "r--", label=f"Ajuste Selection Sort (m={m_selection:.2f})")

    # Configuración del eje X con más marcas para mayor densidad de cuadrícula
    plt.xticks(num_elements, [str(n) for n in num_elements], rotation=45)

    # Activar marcas secundarias (minor ticks) en Y para densificar la cuadrícula logarítmica
    plt.minorticks_on()
    plt.grid(True, which="major", ls="-", alpha=0.7)
    plt.grid(True, which="minor", ls=":", alpha=0.4)

    plt.xlabel("Número de elementos (n) [escala log]")
    plt.ylabel("Tiempo (nanosegundos) [escala log]")
    plt.title("Comparación en Escala Log-Log y Rectas de Ajuste")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
#G4: Comparación de algoritmos de ordenamiento O(n²) y O(n log n) con normalización de tiempos

if seleccion == 10:
    print("--- MENÚ DE GRÁFICOS NORMALIZADOS ---")
    print("1. Algoritmos O(n²) (Bubble, Selection, Insertion) -> Tiempo normalizado: t / n²")
    print("2. Algoritmos O(n log2 n) (Quick Sort, Merge Sort) -> Tiempo normalizado: t / (n log₂ n)")

    opcion_menu = int(input("Ingrese una opción (1 o 2): "))

    # Algoritmos de ordenamiento
    def bubble_sort(A):
        n = len(A)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
        return A

    def insercion_sort(B):
        i = 1
        while i < len(B):
            j = i
            while j > 0 and B[j - 1] > B[j]:
                B[j], B[j - 1] = B[j - 1], B[j]
                j -= 1
            i += 1
        return B

    def selection_sort(C):
        for i in range(len(C) - 1):
            min_idx = i
            for j in range(i + 1, len(C)):
                if C[min_idx] > C[j]:
                    min_idx = j
            if min_idx != i:
                C[min_idx], C[i] = C[i], C[min_idx]
        return C

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

    def merge_sort(E):
        if len(E) <= 1:
            return E
        mid = len(E) // 2
        left = merge_sort(E[:mid])
        right = merge_sort(E[mid:])
        
        result = np.empty(len(E), dtype=E.dtype)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result[k] = left[i]
                i += 1
            else:
                result[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            result[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            result[k] = right[j]
            j += 1
            k += 1
            
        return result

    if opcion_menu == 1:
        num_elements = np.arange(200, 2001, 200)
        size = num_elements.size
        t_bubble = np.zeros(size)
        t_selection = np.zeros(size)
        t_insertion = np.zeros(size)

        for i, n in enumerate(num_elements):
            vector_base = np.random.randint(0, 100, n, dtype=np.int16)

            # Bubble Sort
            vector_test = vector_base.copy()
            t_inicio = perf_counter_ns()
            bubble_sort(vector_test)
            t_final = perf_counter_ns()
            t_bubble[i] = t_final - t_inicio

            # Insertion Sort
            vector_test = vector_base.copy()
            t_inicio = perf_counter_ns()
            insercion_sort(vector_test)
            t_final = perf_counter_ns()
            t_insertion[i] = t_final - t_inicio

            # Selection Sort
            vector_test = vector_base.copy()
            t_inicio = perf_counter_ns()
            selection_sort(vector_test)
            t_final = perf_counter_ns()
            t_selection[i] = t_final - t_inicio

        # Normalización t / n^2
        norm_factor = num_elements ** 2
        plt.plot(num_elements, t_bubble / norm_factor, "g-o", label="Bubble Sort (t / n²)")
        plt.plot(num_elements, t_insertion / norm_factor, "b-o", label="Insertion Sort (t / n²)")
        plt.plot(num_elements, t_selection / norm_factor, "r-o", label="Selection Sort (t / n²)")

        plt.xlabel("Número de elementos (n)")
        plt.ylabel("Tiempo normalizado (t / n²)")
        plt.title("Tiempo Normalizado para Algoritmos O(n²)")
        plt.legend()
        plt.grid(True)
        plt.show()

    elif opcion_menu == 2:
        num_elements = np.arange(1000, 10001, 1000)
        size = num_elements.size
        t_quick_sort = np.zeros(size)
        t_merge_sort = np.zeros(size)

        for i, n in enumerate(num_elements):
            vector_base = np.random.randint(0, 100, n, dtype=np.int16)

            # Quick Sort
            vector_test = vector_base.copy()
            t_inicio = perf_counter_ns()
            quick_sort(vector_test)
            t_final = perf_counter_ns()
            t_quick_sort[i] = t_final - t_inicio

            # Merge Sort
            vector_test = vector_base.copy()
            t_inicio = perf_counter_ns()
            merge_sort(vector_test)
            t_final = perf_counter_ns()
            t_merge_sort[i] = t_final - t_inicio

        # Normalización t / (n * log(n))
        norm_factor = num_elements * np.log2(num_elements)
        plt.plot(num_elements, t_quick_sort / norm_factor, "y-o", label="Quick Sort (t / (n log n))")
        plt.plot(num_elements, t_merge_sort / norm_factor, "m-o", label="Merge Sort (t / (n log n))")

        plt.xlabel("Número de elementos (n)")
        plt.ylabel("Tiempo normalizado (t / (n log₂ n))")
        plt.title("G4: Tiempo Normalizado para Algoritmos O(n log₂ n)")
        plt.legend()
        plt.grid(True)
        plt.show()

    else:
        print("Opción no válida.")
    
#G5: Comparación de casos de entrada (Aleatorio, Ordenado, Inverso) para los algoritmos Bubble Sort, Insertion Sort y Quick Sort

if seleccion == 11:
    print("--- MENÚ DE COMPARACIÓN DE CASOS DE ENTRADA ---")
    print("1. Bubble Sort (Aleatorio, Ordenado, Inverso)")
    print("2. Insertion Sort (Aleatorio, Ordenado, Inverso)")
    print("3. Quick Sort (Aleatorio, Ordenado, Inverso)")
    print("4. Condensado (Todos los algoritmos y casos en una sola gráfica)")
    
    opcion_casos = int(input("Ingrese una opción (1-4): "))

    # Algoritmos de ordenamiento
    def bubble_sort(A):
        n = len(A)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
        return A

    def insercion_sort(B):
        i = 1
        while i < len(B):
            j = i
            while j > 0 and B[j - 1] > B[j]:
                B[j], B[j - 1] = B[j - 1], B[j]
                j -= 1
            i += 1
        return B

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

    num_elements = np.arange(10000, 100001, 10000)
    size = num_elements.size

    # Estructuras para almacenar los tiempos por cada caso
    t_bubble_rand = np.zeros(size)
    t_bubble_sorted = np.zeros(size)
    t_bubble_rev = np.zeros(size)

    t_insert_rand = np.zeros(size)
    t_insert_sorted = np.zeros(size)
    t_insert_rev = np.zeros(size)

    t_quick_rand = np.zeros(size)
    t_quick_sorted = np.zeros(size)
    t_quick_rev = np.zeros(size)

    # Generación y medición de pruebas
    for i, n in enumerate(num_elements):
        v_rand = np.random.randint(0, 100, n, dtype=np.int16)
        v_sorted = np.sort(v_rand)
        v_rev = v_sorted[::-1]

        # --- Bubble Sort ---
        v_test = v_rand.copy()
        t_i = perf_counter_ns()
        bubble_sort(v_test)
        t_bubble_rand[i] = perf_counter_ns() - t_i

        v_test = v_sorted.copy()
        t_i = perf_counter_ns()
        bubble_sort(v_test)
        t_bubble_sorted[i] = perf_counter_ns() - t_i

        v_test = v_rev.copy()
        t_i = perf_counter_ns()
        bubble_sort(v_test)
        t_bubble_rev[i] = perf_counter_ns() - t_i

        # --- Insertion Sort ---
        v_test = v_rand.copy()
        t_i = perf_counter_ns()
        insercion_sort(v_test)
        t_insert_rand[i] = perf_counter_ns() - t_i

        v_test = v_sorted.copy()
        t_i = perf_counter_ns()
        insercion_sort(v_test)
        t_insert_sorted[i] = perf_counter_ns() - t_i

        v_test = v_rev.copy()
        t_i = perf_counter_ns()
        insercion_sort(v_test)
        t_insert_rev[i] = perf_counter_ns() - t_i

        # --- Quick Sort ---
        v_test = v_rand.copy()
        t_i = perf_counter_ns()
        quick_sort(v_test)
        t_quick_rand[i] = perf_counter_ns() - t_i

        v_test = v_sorted.copy()
        t_i = perf_counter_ns()
        quick_sort(v_test)
        t_quick_sorted[i] = perf_counter_ns() - t_i

        v_test = v_rev.copy()
        t_i = perf_counter_ns()
        quick_sort(v_test)
        t_quick_rev[i] = perf_counter_ns() - t_i

    # Visualización según la opción seleccionada
    if opcion_casos == 1:
        plt.plot(num_elements, t_bubble_rand, "g-o", label="Bubble (Aleatorio)")
        plt.plot(num_elements, t_bubble_sorted, "g--s", label="Bubble (Ordenado)")
        plt.plot(num_elements, t_bubble_rev, "g:^", label="Bubble (Inverso)")
        plt.title("Bubble Sort: Comparación según Tipo de Entrada")

    elif opcion_casos == 2:
        plt.plot(num_elements, t_insert_rand, "b-o", label="Insertion (Aleatorio)")
        plt.plot(num_elements, t_insert_sorted, "b--s", label="Insertion (Ordenado)")
        plt.plot(num_elements, t_insert_rev, "b:^", label="Insertion (Inverso)")
        plt.title("Insertion Sort: Comparación según Tipo de Entrada")

    elif opcion_casos == 3:
        plt.plot(num_elements, t_quick_rand, "y-o", label="Quick Sort (Aleatorio)")
        plt.plot(num_elements, t_quick_sorted, "y--s", label="Quick Sort (Ordenado)")
        plt.plot(num_elements, t_quick_rev, "y:^", label="Quick Sort (Inverso)")
        plt.title("Quick Sort: Comparación según Tipo de Entrada")

    elif opcion_casos == 4:
        plt.plot(num_elements, t_bubble_rand, "g-o", label="Bubble (Aleatorio)")
        plt.plot(num_elements, t_bubble_sorted, "g--s", label="Bubble (Ordenado)")
        plt.plot(num_elements, t_bubble_rev, "g:^", label="Bubble (Inverso)")

        plt.plot(num_elements, t_insert_rand, "b-o", label="Insertion (Aleatorio)")
        plt.plot(num_elements, t_insert_sorted, "b--s", label="Insertion (Ordenado)")
        plt.plot(num_elements, t_insert_rev, "b:^", label="Insertion (Inverso)")

        plt.plot(num_elements, t_quick_rand, "y-o", label="Quick Sort (Aleatorio)")
        plt.plot(num_elements, t_quick_sorted, "y--s", label="Quick Sort (Ordenado)")
        plt.plot(num_elements, t_quick_rev, "y:^", label="Quick Sort (Inverso)")
        plt.title("Comparativo Condensado: Algoritmos y Tipos de Entrada")

    else:
        print("Opción no válida.")

    if opcion_casos in [1, 2, 3, 4]:
        plt.xlabel("Número de elementos (n)")
        plt.ylabel("Tiempo (nanosegundos)")
        plt.legend()
        plt.grid(True)
        plt.show()
        
#G6: Comparación de Quick Sort según el rango de valores

if seleccion == 12:
    print("--- COMPARACIÓN DE QUICKSORT SEGÚN EL RANGO DE VALORES ---")

    # Algoritmo de ordenamiento Quick Sort (mediana de tres)
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

    num_elements = np.arange(1000, 10001, 1000)
    size = num_elements.size

    t_quick_small_range = np.zeros(size)  # Rango 0 a 99 (int16)
    t_quick_large_range = np.zeros(size)  # Rango 0 a 10^6 (int32)

    for i, n in enumerate(num_elements):
        # Generación de vectores con distintos rangos de datos
        v_small = np.random.randint(0, 100, n, dtype=np.int16)
        v_large = np.random.randint(0, 1000001, n, dtype=np.int32)

        # Medición para rango pequeño (0–99)
        v_test = v_small.copy()
        t_i = perf_counter_ns()
        quick_sort(v_test)
        t_quick_small_range[i] = perf_counter_ns() - t_i

        # Medición para rango grande (0–10^6)
        v_test = v_large.copy()
        t_i = perf_counter_ns()
        quick_sort(v_test)
        t_quick_large_range[i] = perf_counter_ns() - t_i

    # Graficación de resultados
    plt.plot(num_elements, t_quick_small_range, "y-o", label="Quick Sort (Rango 0 - 99)")
    plt.plot(num_elements, t_quick_large_range, "c--s", label="Quick Sort (Rango 0 - 10⁶)")

    plt.xlabel("Número de elementos (n)")
    plt.ylabel("Tiempo (nanosegundos)")
    plt.title("Impacto del Rango de Valores en Quick Sort")
    plt.legend()
    plt.grid(True)
    plt.show()