# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 23:29:09 2020

@author: saiprasadparsa"""

import time
import numpy as np
from  matplotlib import pyplot as plt
import copy
import sys
sys.setrecursionlimit(50000)
import threading
import random


def run():
    samples=(5000,10000,15000,20000,25000,30000)
    
    def insertion_sort(data):
        start_time=time.time()
        
        for j in range(1,(len(data)),1):
            key=data[j]
            i=j-1
            while i>=0 and data[i]>key:
                data[i+1]=data[i]
                i=i-1
            data[i+1]=key
        
        end_time = time.time()
        duration = end_time-start_time
        
        return duration,data
        
    def singlepivot_QS(data):
        
        start_time=time.time()
        
        def partition(A, p, r):
        
            x = A[r]
            i = p-1
            for j in range(p,r):   
                if A[j]<=x:
                    i+=1
                    A[i],A[j]=A[j],A[i]
            A[i+1],A[r]=A[r],A[i+1]
            return i+1
        
        
    
        def randomized_partition(A, p, r):
            
            i = random.randrange(p,r+1)
            
            A[r],A[i]=A[i],A[r]
            return partition(A,p,r)
            
            
        def randomized_quicksort(A,p,r):
            
            if p<r:
                q= randomized_partition(A,p,r)
                randomized_quicksort(A,p,q-1)
                randomized_quicksort(A,q+1,r)
                
        p=0
        r= len(data)-1     
        randomized_quicksort(data,p,r)
    
        end_time = time.time()
        duration = end_time-start_time
        
                
        return duration,data
    
    
    def d_singlepivot_QS(data):
        start_time=time.time()
        def dual_pivot_sort(A, start, stop):
                if top <= start:
                    return
                p = start
                q = top
                k = p+1
                h = k
                l = q-1
                if A[p] > A[q]:
                    A[p], A[q] = A[q], A[p]
                while k <= l:     
                    if A[k] < A[p]:
                        A[h], A[k] = A[k], A[h]
                        h += 1 
                        k += 1 
                    elif A[k] > A[q]:
                        A[k], A[l] = A[l], A[k]
                        l -= 1 
                    else: k += 1
                h -= 1
                l += 1 
                A[p], A[h] = A[h], A[p]
                A[q], A[l] = A[l], A[q]
                dual_pivot_sort(A, start, h-1)
                dual_pivot_sort(A, h+1, l-1)
                dual_pivot_sort(A, l+1, top)
                
        p=0
        r= len(data)-1     
        dual_pivot_sort(data,p,r)
    
        end_time = time.time()
        duration = end_time-start_time
        return duration,data
    
    def random_generator(n):
        x=[]
        for i in range(1,n+1):        
            x.append(int(np.random.uniform(0,n)))#to generate random numbers of required size
            
        return x
            
    def generate_plots(insertion,quick,d_quick,Plot_name):
        
        plt.plot(samples,insertion,label='Insertion sort')
        plt.plot(samples,quick, label='Quick Single Pivot sort')
        plt.plot(samples,d_quick, label='Quick Double Pivot sort')
        plt.xlabel('Number of samples')
        plt.ylabel('Recorded Duration')
        plt.title(Plot_name)
        plt.legend()
        plt.show()
        
        
            
            
    def input_1():
        runs=3
        
        quick_duration=[]   # To store averaged time durations per each saple size
        d_quick_duration=[]
        insertion_duration=[] # To store averaged time durations per each sample size
        d_quick_total=0
        quick_total=0  #To store sum of time durations per run
        insertion_total=0 # to store sum of time duratiobs per run
        for n in samples:
            #print(n)        
            for run in range(runs):
                data=random_generator(n)
                data_copy = data.copy()
                data_copy1 = data.copy()
                quick_total += singlepivot_QS(data)[0]
                d_quick_total += d_singlepivot_QS(data_copy1)[0]
                insertion_total += insertion_sort(data_copy)[0]
            quick_duration.append( quick_total/3 )
            d_quick_duration.append( d_quick_total/3 )
            insertion_duration.append( insertion_total/3 )
            quick_total=0
            d_quick_total=0
            insertion_total=0
        generate_plots(insertion_duration,quick_duration,d_quick_duration,"Input/plot1")
        
                
    
            
    def input_2():
        
        runs=3
        
        quick_duration=[]   # To store averaged time durations per each saple size
        d_quick_duration=[]
        insertion_duration=[] # To store averaged time durations per each sample size
        quick_total=0  #To store sum of time durations per run
        d_quick_total=0
        insertion_total=0 # to store sum of time duratiobs per run
        for n in samples:
            #print(n)        
            for run in range(runs):
                data=random_generator(n)
                data=sorted(data)
                data_copy = data.copy()
                data_copy1 = data.copy()
                #print(data_copy)
                quick_total += singlepivot_QS(data)[0]
                d_quick_total += d_singlepivot_QS(data_copy1)[0]
                insertion_total += insertion_sort(data_copy)[0]
            quick_duration.append( quick_total/3 )
            d_quick_duration.append( d_quick_total/3 )
            insertion_duration.append( insertion_total/3 )
            quick_total=0
            d_quick_total=0
            insertion_total=0
        generate_plots(insertion_duration,quick_duration,d_quick_duration,"Input/plot2")
       
    
    def input_3():
        
         
        runs=3
        
        quick_duration=[]   # To store averaged time durations per each saple size
        d_quick_duration=[] 
        insertion_duration=[] # To store averaged time durations per each sample size
        quick_total=0  #To store sum of time durations per run
        d_quick_total=0
        insertion_total=0 # to store sum of time duratiobs per run
        for n in samples:
            #print(n)        
            for run in range(runs):
                data = random_generator(n)
                data = sorted(data,reverse=True)# sorting data in reverse order to generate worst case scenario
                data_copy = data.copy()
                data_copy1 = data.copy()
                quick_total += singlepivot_QS(data)[0]
                d_quick_total += d_singlepivot_QS(data_copy1)[0]
                insertion_total += insertion_sort(data_copy)[0]
            quick_duration.append( quick_total/3 )
            d_quick_duration.append( d_quick_total/3 )
            insertion_duration.append( insertion_total/3 )
            quick_total=0
            d_quick_total=0
            insertion_total=0
        generate_plots(insertion_duration,quick_duration,d_quick_duration,"Input/plot3")
        
    
    
    
    
    def input_4():
        
        
        runs=3
        
        quick_duration=[]   # To store averaged time durations per each saple size
        d_quick_duration=[]
        insertion_duration=[] # To store averaged time durations per each sample size
        quick_total=0  #To store sum of time durations per run
        d_quick_total=0
        insertion_total=0 # to store sum of time duratiobs per run
        for n in samples: # looping over range of samples
            #print(n)        
            for run in range(runs): #looping over 3 runs per each 
                
                data = random_generator(n)
                data = sorted(data)    # sorting the data to generate best case scenario
                
                for noise_count in range(50):
                    
                    noise = np.random.randint(0,n,2)                
                    temp = data[noise[0]]
                    data[noise[0]] = data[noise[1]]
                    data[noise[1]] = temp
                    
                data_copy = data.copy()
                data_copy1 = data.copy()
                
                quick_total += singlepivot_QS(data)[0]
                d_quick_total += d_singlepivot_QS(data_copy1)[0]
                insertion_total += insertion_sort(data_copy)[0]
                
            #print(quick_total/3, insertion_total/3 )
                
            quick_duration.append( quick_total/3 )
            d_quick_duration.append( d_quick_total/3 )
            insertion_duration.append( insertion_total/3 )
            quick_total=0
            d_quick_total=0
            insertion_total=0
            
        generate_plots(insertion_duration,quick_duration,d_quick_duration,"Input/plot4")
        
        
    def input_5():
        runs=3
        
        quick_duration=[]   # To store averaged time durations per each saple size
        d_quick_duration=[]
        insertion_duration=[] # To store averaged time durations per each sample size
        d_quick_total=0
        quick_total=0  #To store sum of time durations per run
        insertion_total=0 # to store sum of time duratiobs per run
        for n in samples:
            #print(n)        
            for run in range(runs):
                data=np.ones(n)
                data=list(data)
                data_copy = data.copy()
                data_copy1 = data.copy()
                quick_total += singlepivot_QS(data)[0]
                d_quick_total += d_singlepivot_QS(data_copy1)[0]
                insertion_total += insertion_sort(data_copy)[0]
            quick_duration.append( quick_total/3 )
            d_quick_duration.append( d_quick_total/3 )
            insertion_duration.append( insertion_total/3 )
            quick_total=0
            d_quick_total=0
            insertion_total=0
        generate_plots(insertion_duration,quick_duration,d_quick_duration,"Input/plot5")
        
    def input_6():
        
        runs=100000
        
        
        quick_total=0
        d_quick_total=0
        insertion_total=0
               
        for run in range(runs):
            #print(run)
            data = random_generator(50)
            data_copy = data.copy()
            data_copy1 = data.copy()
            quick_total += singlepivot_QS(data)[0]
            d_quick_total += d_singlepivot_QS(data_copy1)[0]
            insertion_total += insertion_sort(data_copy)[0]
    
        print(quick_total,d_quick_total,insertion_total)
        
    
         
    input_3()        
            
threading.stack_size(int(1e8))
t= threading.Thread(target=run)
t.start()
t.join()            
        