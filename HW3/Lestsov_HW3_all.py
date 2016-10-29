import pandas as pd
import numpy as np


house_prices = pd.read_csv('house_prices.csv')

# Task 1
quantiles = np.linspace(0,1,5)
quantile_ranges = house_prices["SalePrice"].quantile(quantiles)
groups = house_prices.groupby(pd.cut(house_prices["SalePrice"], quantile_ranges))

print "Data frame, divided into quartiles:"
for gr, df in groups:
    print gr
    print df.head()

# Task 2
print "Mean in YearBuilt:"
for gr, df in groups:
    print "{:16} : {}".format(gr, df["YearBuilt"].mean())
    
print "Mean in KitchenAbvGr:"
for gr, df in groups:
    print "{:16} : {}".format(gr, df["KitchenAbvGr"].mean())

func_group = house_prices.groupby("Functional")
for gr, df in func_group:
    print "{:8} : {}".format(gr, df["SalePrice"].mean())