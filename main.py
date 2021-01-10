import pickle
from scipy.optimize import curve_fit
import numpy as np
import random


def getFluorescenceSignal(lifetime, A, t):
    signal = A * np.exp(- t / lifetime)
    return signal

def getFluorescenceSignalSecond(f, A, t):
    lifetime = - t / np.log(f/A)
    return lifetime


# reading mixture 1
infile = open("mixture1.dat", 'rb')
mixture1 = pickle.load(infile, encoding='bytes')
infile.close()
# reading mixture 2
infile = open("mixture2.dat", 'rb')
mixture2 = pickle.load(infile, encoding='bytes')
infile.close()
# reading mixture 3
infile = open("mixture3.dat", 'rb')
mixture3 = pickle.load(infile, encoding='bytes')
infile.close()
# reading mixture 4
infile = open("mixture4.dat", 'rb')
mixture4 = pickle.load(infile, encoding='bytes')
infile.close()

lifetime_list = [5.8, 8.9, 38.6, 57.8, 200.9, 516.2]
A_list = [1, 2, 3]
init_vals = [ random.choice(A_list), 5*0.0000000001]

floatList = []

for i in mixture1:
    floatList.append(float(i))

best_vals, covar  = curve_fit(getFluorescenceSignalSecond, floatList[9999], lifetime_list, p0=A_list)

print(best_vals)
