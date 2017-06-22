import pandas as pd
import numpy as np
import statistics as st
from scipy.stats import norm

scores = pd.read_csv("07_klout_scores.csv", header=None)


def get_SE(pop_std, n):
    #SE, standard error = standard deviation of distribution of sample means
    #central limit theorum
    SE = pop_std/np.sqrt(n)
    return(SE)

def get_pop_sd(SE, n):
    pop_std = SE*np.sqrt(n)
    return(pop_std)

def get_z(x, avg, std):
    z = (x-avg)/std
    return(z)

def get_p_greater_from_x(x, avg, std):
    z = get_z(x, avg, std)
    p = 1 - norm.cdf(z)
    return(p)

pop_std = get_pop_sd(SE=10, n=4)
print(pop_std)

SE = get_SE(pop_std, 16)
print(SE)

biebz = get_z(x=40, avg=37.72, std=SE)
print(biebz)

p = 1-norm.cdf(biebz)
print(p)

klout = pd.read_csv("C:/Users/Laptop/Downloads/Klout scores (Lesson 7) - Sheet1.csv", names=["score"])

#print(klout[['score']].head())

avg = klout[["score"]].mean()
std = klout[["score"]].std()
#pop_std = st.pstdev(klout[["score"]])
#print(avg)
#print(std)


# SE = get_SE(pop_std=20, n=25)
# print(get_z(x=104, avg=100, std=SE))
# SE = get_SE(pop_std=20, n=100)
# print(get_z(x=104, avg=100, std=SE))
# SE = get_SE(pop_std=20, n=100)
# print(get_z(x=102, avg=100, std=SE))
# SE = get_SE(pop_std=20, n=25)
# print(get_z(x=102, avg=100, std=SE))
SE = get_SE(pop_std=20, n=10)
print(SE)
p = get_p_greater_from_x(x=110, avg=100, std=SE)
print(p)

fb = pd.read_csv("C:/Users/Laptop/Downloads/Facebook Friends - Problem Set 7 - Sheet1.csv", header=0, names=["friends"])
pop_std = np.std(fb["friends"])
print(pop_std)
SE = get_SE(pop_std, n=10)
print(SE)
