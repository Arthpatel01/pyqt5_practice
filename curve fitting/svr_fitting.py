import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
import pandas as pd
import json

df = pd.read_csv("longley.csv", header=None)

df_values = df.values

x, y = df_values[:, 4], df_values[:, -1]
print("x: ", x)
print("y: ", y)

voltage_data = x.reshape(-1, 1)
length_data = y.reshape(-1, 1)

svr_model = SVR(kernel="linear")
svr_model.fit(X=voltage_data, y=length_data)

plt.scatter(voltage_data, length_data, label="Calibration Data")
# plt.scatter(voltage_data, svr_model.predict(voltage_data), marker="d", color="yellow")
plt.plot(voltage_data, svr_model.predict(voltage_data), color="red", label="SVR Predicted Data")
plt.xlabel("Voltage")
plt.ylabel("Length")
plt.legend()
plt.show()

slope = svr_model.coef_[0][0]
intercept = svr_model.intercept_[0]
print("\n\nSVR Prediction:", svr_model.predict([[123.366]]))
with open("slope_params_svr.json", "w") as file:
    json.dump({"param_slope": slope, "param_intercept": intercept}, file)
