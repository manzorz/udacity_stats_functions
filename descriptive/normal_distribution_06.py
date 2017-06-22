import numpy as np
#import pandas as pd
from scipy.stats import norm
#get z from probability = norm.ppf()
#get probability from z = norm.cdf()
def get_z(x, avg, std):
    z = (x-avg)/std
    return(z)

def get_x(z, avg, std):
    x = z*std+avg
    return(x)

def get_std(x, z, avg):
    std = (x-avg)/z
    return(std)

def get_p_from_x(x, avg, std):
    z = get_z(x, avg, std)
    p = norm.cdf(z)
    return(p)

def use_top_percentile_for_x(top_percentile, avg, std):
    percent_less = 1 - top_percentile
    z = norm.ppf(percent_less)
    x = get_x(z, avg, std)
    return(x)

def get_z_from_p(p):
    z = norm.ppf(p)
    return(z)

def get_p_greater_from_x(x, avg, std):
    z = get_z(x, avg, std)
    p = 1 - norm.cdf(z)
    return(p)

def get_x_from_top_percentile(pct, avg, std):
    pct = pct/100 if pct > 1 else pct
    p = 1 - pct
    z = get_z_from_p(p)
    x = get_x(z, avg, std)
    return(x)
