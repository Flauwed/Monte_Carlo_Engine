import numpy as np

# This is a basic test to make sure my .venv is set up correctly. 

A = np.array([[1,89,4],[6,54,27],[9,10,-62]])

B = A @ A.T

A_inv = np.linalg.inv(A)

print(A_inv @ A)
print(np.eye(np.shape(A)[0]))