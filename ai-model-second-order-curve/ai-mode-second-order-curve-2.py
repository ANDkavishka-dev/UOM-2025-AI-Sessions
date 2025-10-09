import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

# ===============================
# Load Dataset
# ===============================
data = pd.read_csv('C:\\Users\\USER\\UOM-2025-AI-Sessions\\test_second_order.csv')
print(data)

x = data['Testing x values (x_units)'].values.reshape(-1,1)
y = data['Testing y vales (y_units)'].values

# ===============================
# Create Quadratic Feature
# ===============================
x_quad = np.column_stack((x, x**2))   # [x, x²]
print("Input shape:", x_quad.shape)

# ===============================
# Initialize Neural Network
# ===============================
max_iter = 1000
learning_rate = 0.01

nn_model = MLPRegressor(hidden_layer_sizes=(1,), 
                        max_iter=max_iter,
                        learning_rate_init=learning_rate,
                        solver='sgd',
                        random_state=1)

# ===============================
# Initial Training
# ===============================
nn_model.fit(x_quad, y)

# ===============================
# Track Loss with Partial Fit
# ===============================
loss_values = []
for i in range(max_iter):
    nn_model.partial_fit(x_quad, y)
    y_pred_partial = nn_model.predict(x_quad)
    loss = np.mean((y - y_pred_partial) ** 2)
    loss_values.append(loss)

# ===============================
# Extract Weights and Biases
# ===============================
w_input_hidden = nn_model.coefs_[0]   # shape (2,1) → [x, x²] → hidden
w_hidden_output = nn_model.coefs_[1]  # shape (1,1) → hidden → output
b_hidden = nn_model.intercepts_[0]    # bias for hidden
b_output = nn_model.intercepts_[1]    # bias for output

print("Weights input-hidden:", w_input_hidden)
print("Weight hidden-output:", w_hidden_output)
print("Hidden bias:", b_hidden)
print("Output bias:", b_output)

# ===============================
# Compute Equivalent Quadratic Equation
# ===============================
a = w_input_hidden[1][0] * w_hidden_output[0][0]   # coefficient of x²
b = w_input_hidden[0][0] * w_hidden_output[0][0]   # coefficient of x
c = b_hidden[0] * w_hidden_output[0][0] + b_output[0]   # constant term

print("Quadratic coefficients:")
print("a =", a, "b =", b, "c =", c)

# ===============================
# Final Predictions
# ===============================
y_pred = nn_model.predict(x_quad)

# Now you can plot loss_values or (x,y,y_pred) if needed

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