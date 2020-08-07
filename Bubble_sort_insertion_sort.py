# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 23:29:09 2020

@author: saiprasadparsa"""

import time
import numpy as np
from  matplotlib import pyplot as plt
import copy

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
    

def bubble_sort(data):
    size=len(data)
    start_time=time.time()
    for i in range(size):
        swap=False
        for j in range(size-1-i):  # As we start sorting the last elements get sorted i.e,i elements are already sorted for every cycle , we can ignore them.                                  
            if data[j]>=data[j+1]:                
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
                swap=True
        if not swap:
            break
    end_time = time.time()
    duration = end_time-start_time
    
    return duration,data

def random_generator(n):
    x=[]
    for i in range(1,n+1):        
        x.append(int(np.random.uniform(0,n)))#to generate random numbers of required size
        
    return x
        
def generate_plots(insertion,bubble,Plot_name):
    
    plt.plot(samples,insertion,label='Insertion sort')
    plt.plot(samples,bubble, label='Bubble sort')
    plt.xlabel('Number of samples')
    plt.ylabel('Recorded Duration')
    plt.title(Plot_name)
    plt.legend()
    plt.show()
    
    
        
        
def input_1():
    runs=3
    
    bubble_duration=[]   # To store averaged time durations per each saple size
    insertion_duration=[] # To store averaged time durations per each sample size
    bubble_total=0  #To store sum of time durations per run
    insertion_total=0 # to store sum of time duratiobs per run
    for n in samples:
        #print(n)        
        for run in range(runs):
            data=random_generator(n)
            data_copy = data.copy()
            bubble_total += bubble_sort(data)[0]
            insertion_total += insertion_sort(data_copy)[0]
        bubble_duration.append( bubble_total/3 )
        insertion_duration.append( insertion_total/3 )
        bubble_total=0
        insertion_total=0
    generate_plots(insertion_duration,bubble_duration,"Input/plot1")
    
            

        
def input_2():
    
    runs=3
    
    bubble_duration=[]   # To store averaged time durations per each saple size
    insertion_duration=[] # To store averaged time durations per each sample size
    bubble_total=0  #To store sum of time durations per run
    insertion_total=0 # to store sum of time duratiobs per run
    for n in samples:
        #print(n)        
        for run in range(runs):
            data=random_generator(n)
            data=sorted(data)
            data_copy = data.copy
            #print(data_copy)
            bubble_total += bubble_sort(data)[0]
            insertion_total += insertion_sort(data_copy)[0]
        bubble_duration.append( bubble_total/3 )
        insertion_duration.append( insertion_total/3 )
        bubble_total=0
        insertion_total=0
    generate_plots(insertion_duration,bubble_duration,"Input/plot2")
   

def input_3():
    
     
    runs=3
    
    bubble_duration=[]   # To store averaged time durations per each saple size
    insertion_duration=[] # To store averaged time durations per each sample size
    bubble_total=0  #To store sum of time durations per run
    insertion_total=0 # to store sum of time duratiobs per run
    for n in samples:
        #print(n)        
        for run in range(runs):
            data = random_generator(n)
            data = sorted(data,reverse=True)# sorting data in reverse order to generate worst case scenario
            data_copy = data.copy()
            
            bubble_total += bubble_sort(data)[0]
            insertion_total += insertion_sort(data_copy)[0]
        bubble_duration.append( bubble_total/3 )
        insertion_duration.append( insertion_total/3 )
        bubble_total=0
        insertion_total=0
    generate_plots(insertion_duration,bubble_duration,"Input/plot3")
    




def input_4():
    
    
    runs=3
    
    bubble_duration=[]   # To store averaged time durations per each saple size
    insertion_duration=[] # To store averaged time durations per each sample size
    bubble_total=0  #To store sum of time durations per run
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
            
            bubble_total += bubble_sort(data)[0]
            insertion_total += insertion_sort(data_copy)[0]
            
        #print(bubble_total/3, insertion_total/3 )
            
        bubble_duration.append( bubble_total/3 )
        insertion_duration.append( insertion_total/3 )
        bubble_total=0
        insertion_total=0
        
    generate_plots(insertion_duration,bubble_duration,"Input/plot4")
    
    
       
def input_5():
    
    runs=100000
    
    
    bubble_total=0
    insertion_total=0
           
    for run in range(runs):
        #print(run)
        data = random_generator(50)
        data_copy = data.copy()
        
        bubble_total += bubble_sort(data)[0]
        insertion_total += insertion_sort(data_copy)[0]

    print(bubble_total,insertion_total)
    
input_1() 
input_2()        
input_3() 
input_4() 
input_5() 
        
        
        
        
        
        