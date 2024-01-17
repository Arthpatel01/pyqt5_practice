import json

import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

filename = "longley.csv"

df = pd.read_csv(filename, header=None)

data = df.values

x, y = data[:, 4], data[:, -1]


# plt.scatter(x=x, y=y)
# plt.show()


def objective(x, a, b):
    return a * x + b


popt, _ = curve_fit(objective, x, y)

a, b = popt
print(f"y = {a}*x + {b}")

plt.scatter(x, y)

x_line = np.arange(min(x), max(x), 1)
y_line = objective(x_line, a, b)

plt.plot(x_line, y_line, "--", color="red")
plt.show()

print("Fit Curve Prediction:", objective(123.366, a, b))

with open("curve_param.json", "w") as file:
    json.dump({"slope": a, "intercept": b}, file)
