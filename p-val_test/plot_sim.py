import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)
import pandas as pd
import collections
import sys
import numpy as np
import math

k=13
x=20000
n = 1000   # number of trials, probability of each trial
p = float(1) - math.pow((1-(1/math.pow(4,k))),x)


s = np.random.binomial(n, p, 10000)


sum_file = sys.argv[1]

df = pd.read_csv(sum_file,header=None,sep='\t')

sns.distplot(df[0], axlabel='kmer matches',label="simulation")

sns.distplot(s, label="binomial", hist=False)

#g.set_axis_labels(x_var='kmer matches')

plt.legend()

plt.savefig("./sim.pdf", format="pdf")
