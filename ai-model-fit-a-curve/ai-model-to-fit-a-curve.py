import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

data=pd.read_csv('C:\\Users\\USER\\UOM-2025-AI-Sessions\\session-0\\files\\data.csv')
print(data)

x=data['Circuit Current (Ic_A)'].values.reshape(-1,1)
print(x)

y=data['Terminal Voltage (Vt_V)'].values
print(y)

x_1 = x[:]
y_1 = y[:]


# plot of data points
'''
plt.figure(0)
plt.scatter(x,y)
plt.xlabel('Circuit Current (Ic_A)')
plt.ylabel('Terminal Voltage (Vt_V)')
plt.title('Dataset')
plt.grid(True)
plt.show(block=False)
'''

max_iter=1000
learning_rate=0.01

nn_model=MLPRegressor(hidden_layer_sizes=(1,),max_iter=max_iter,learning_rate_init=learning_rate)

nn_model.fit(x,y)

loss_values=[]
for i in range(max_iter):
  nn_model.partial_fit(x,y)
  y_pred_partial=nn_model.predict(x)
  loss=np.mean((y-y_pred_partial)**2)
  loss_values.append(loss)


# plot of Loss value

plt.figure(1)
plt.scatter(range(max_iter),loss_values)
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Loss Curve')
plt.grid(True)
plt.show()



weight_1=nn_model.coefs_[0]
print('Weight_1:',weight_1)

weight_2=nn_model.coefs_[1]
print('Weight_2:',weight_2)

bias_1=nn_model.intercepts_[0]
print('Bias_1:',bias_1)

bias_2=nn_model.intercepts_[1]
print('Bias_2:',bias_2)

m=weight_1*weight_2
c=bias_1*weight_2+bias_2
print('m:',m)
print('c:',c)


#

plt.scatter(x,y,label='Actual')
plt.plot(x,y_pred_partial, color='red', label='Predicted')
plt.xlabel('Circuit Current (Ic_A)')
plt.ylabel('Terminal Voltage (Vt_V)')
plt.title('Actual vs Predicted')
plt.legend()
plt.grid(True)
plt.show()



#---------------------Plots--------------------------
fig, axs = plt.subplots(1, 3, figsize=(8,2))

# ----------------First Sub-plot---------------------
axs[0].scatter(x,y)
axs[0].set_xlabel('Circuit Current (Ic_A)')
axs[0].set_ylabel('Terminal Voltage (Vt_V)')
axs[0].set_title('Dataset')
axs[0].grid(True)

# ----------------Second Sub-plot---------------------
axs[1].scatter(range(max_iter),loss_values)
axs[1].set_xlabel('Iteration')
axs[1].set_ylabel('Loss')
axs[1].set_title('Loss Curve')
axs[1].grid(True)

# -----------------Third Sub-plot---------------------
axs[2].scatter(x,y,label='Actual')
axs[2].plot(x,y_pred_partial, color='red', label='Predicted')
axs[2].set_xlabel('Circuit Current (Ic_A)')
axs[2].set_ylabel('Terminal Voltage (Vt_V)')
axs[2].set_title('Actual vs Predicted')
axs[2].legend()
axs[2].grid(True)

plt.show()