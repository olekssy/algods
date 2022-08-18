""" A primer of linear optimization with numpy and scipy. """

import numpy as np
import scipy

# === System of equations ===
# 5x + 3y = 13
# -7x + 17y = 23

# numpy inverse
A = np.array([[5, 3], [-7, 17]])
B = np.array([13, 23])
X = np.linalg.inv(A) @ B
print(X)

# numpy solve
X = np.linalg.solve(A, B)
print(X)

# scipy
X = scipy.linalg.solve(A, B)
print(X)

# === Linear programming ===
# solve equation subject to constraints
# 3x + 12y = 1000
# given
# 30 < x < 160
# 10 < y < 60
# x + y > 180
c = np.ones(2)  # find X to min c @ X, where X = (x, y)
A_eq = np.array([[3, 12]])  # A_eq @ X = b_eq
b_eq = np.array([1000])
A_ub = np.array([[-1, -1]])  # -x -y <= 180
b_ub = np.array([-180])  # A_ub @ X = b_ub
bounds = np.array([[30, 160], [10, 60]])  # a < X < b, c < Y < d
ans = scipy.optimize.linprog(c=c,
                             A_ub=A_ub,
                             A_eq=A_eq,
                             b_ub=b_ub,
                             b_eq=b_eq,
                             bounds=bounds)
print(ans.x)

# === System of inequalities ===
# compute asset weights maximizing return
# mu = [0.05, 0.1]
# subject to
# w1 + w2 = 1
# w1 > 0.3
# w2 > 0.0
c = np.array([-0.05, -0.1])
A_eq = np.array([[1, 1]])
b_eq = np.array([1])
bounds = np.array([[0.3, 1], [0, 1]])
res = scipy.optimize.linprog(c=c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
print(res.x)
