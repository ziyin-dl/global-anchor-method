import numpy as np

n = 100
k = 20
A = np.random.normal(0, 1, size=(n, n))
U, D, V = np.linalg.svd(A)
E = np.random.normal(0, 0.1, size=(n, n))
A_tilde = A + E
U_tilde, D_tilde, V_tilde = np.linalg.svd(A_tilde)

E = U[:,:k]
F = U_tilde[:,:k]

U, C, V = np.linalg.svd(E.T.dot(F))
S = np.sqrt(1 - C ** 2)
Theta = np.arccos(C)
Q = V.T.dot(U.T)

align = np.linalg.norm(E-F.dot(Q), 'fro')
half_theta = np.linalg.norm(np.sin(Theta / 2))
anchor = np.linalg.norm(E.dot(E.T) - F.dot(F.T), 'fro')
theta = np.linalg.norm(np.sin(Theta))

print("anchoring: {} {}".format(anchor, np.sqrt(2) * theta))
print("alignment: {} {}".format(align, 2 * half_theta))
