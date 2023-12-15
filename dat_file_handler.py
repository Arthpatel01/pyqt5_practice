import pandas as pd
import os

filename = "test_dat_file.dat"

df = pd.read_csv(filename)

for row in df:
    print(row)

print(df.head())
print(df.describe())
