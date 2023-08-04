"""
Calculadora desafio Data Talks
"""

#Packages:
import statistics as stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#-----------------------------------
#Functions:
def average(list):
    out = 0
    for value in list:
        out += value
    
    return out / len(list)

def amplitude(list):
    amp = 0.0
    amp = max(list) - min(list)
    
    return amp

def menu():
    print('[1] - frequency mesures')
    print('[2] - central tendency mesures')
    print('[3] - dispertion mesures')
    print('[4] - position mesures')
    print('[5] - discribe data')
    print('[6] - exit')
    
def boxplot(list):
    plt.figure(figsize = (11, 6))
    
    sns.set_style("whitegrid")
    
    ax = sns.boxplot(data=list)
    
    plt.title("List Boxplot", loc="center", fontsize=18)
#    plt.xlabel("Tipos de Flores")
    plt.ylabel("List range")

    plt.show(ax)

def quantis(list):
    x = [i for i in range(len(list))]
    df = pd.DataFrame(x)
    
    return df

def histogram(list):
    np.random.seed(19680801)

    # example data
    mu = average(any_list)  # mean of distribution
    sigma = stats.stdev(any_list)  # standard deviation of distribution
    x = mu + sigma * np.random.randn(437)

    num_bins = len(list)

    fig, ax = plt.subplots()

    # the histogram of the data
    n, bins, patches = ax.hist(x, num_bins, density=True)

    # add a 'best fit' line
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
         np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
    ax.plot(bins, y, '--')
    ax.set_xlabel('Smarts')
    ax.set_ylabel('Probability density')
    ax.set_title(r'Histogram')

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    plt.show()
        
#-----------------------------------
#List:
any_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#-----------------------------------
#Loop:
    
valor_menu = 'Inicial'
while valor_menu in (1, 2, 3, 4, 5, 'Inicial'):
    menu()
    valor_menu = int(input('Entre a opção desejada: '))
    
    if valor_menu == 1:
        histogram(any_list)
        
        print('-----------------------------------------------------------')
        print('MEW MENU')
        
    if valor_menu == 2:
        print('List average: ' + str(average(any_list)))
        print('List median: ' + str(stats.median(any_list)))
        print('List mode: ' + str(stats.mode(any_list)))
        
        print('-----------------------------------------------------------')
        print('MEW MENU')
    
    if valor_menu == 3:
        print('List amplitude: ' + str(amplitude(any_list)))
        print('List standard deviation: ' + str(stats.stdev(any_list)))
        print('List variance1: ' + str(stats.variance(any_list)))
        
        print('-----------------------------------------------------------')
        print('MEW MENU')
        
    if valor_menu == 4:
        boxplot(any_list)
        print('First Quartile: ' + str(quantis(any_list).quantile(.25).name))
        print('Second Quartile: ' + str(quantis(any_list).quantile(.5).name))
        print('Third Quartile: ' + str(quantis(any_list).quantile(.75).name))
        
        print('-----------------------------------------------------------')
        print('MEW MENU')
        
    if valor_menu == 5:
        print('discribe data')

