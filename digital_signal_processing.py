## Problem 2.3 — The Digital Signal Processing Pipeline 
## inputs: N-samples, sensor readings, 
## libraries
import numpy as np
import math 
## input validation
while True:
    try:
        n=int(input("Please input the number of samples:"))
    except ValueError:
        print("Please input valid number of samples.")
        continue
    if n <= 0:
        print("Please input number greater than 0.")
        continue
    break

def get_values(text):
    while True:
        try:
            value= float(input(text))
        except ValueError:
            print("Please input valid sensor value.")
            continue
        return value
## sensor values inputs        
samples = []
for i in range(n):
    value = get_values(f'Please input the value for sensor {i+1}:')
    samples.append(value)
 
## outputs   
print(samples)
    
samples= np.array(samples)
meanSamples = np.mean(samples)
print(f'The mean of the samples is {meanSamples:.2f}.')

dcCompo = samples - meanSamples
print(f'The DC components are {dcCompo}.')

sqrValue = dcCompo ** 2
print (f'The square value are {sqrValue}.')

meanSqrValue = np.mean(sqrValue)
print(f'The mean square value is {meanSqrValue:.2f}')

RMS = math.sqrt(meanSqrValue)
print(f'The RMS of the system is {RMS:.2f}.') 