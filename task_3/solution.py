import numpy as np

# Задача 3: Найти токи I из матричного уравнения RI = U
# для i от 5 до 80, j от 5 до 80

# Размер матрицы: i и j от 5 до 80 включительно
indices = list(range(5, 81))  # 5..80
n = len(indices)  # 76

# Матрица сопротивлений R
# R_{i,j} = cos(j) * (i + j),  если i == j
#           1,                  если i == j + 1
#           0,                  иначе
R = np.zeros((n, n))
for row, i in enumerate(indices):
    for col, j in enumerate(indices):
        if i == j:
            R[row, col] = np.cos(j * (i + j))
        elif i == j + 1:
            R[row, col] = 1

# Вектор напряжений U
# U_i = i
U = np.array([float(i) for i in indices])

# Решение: RI = U => I = R^{-1} * U
I = np.linalg.solve(R, U)

print("Токи I (для i от 5 до 80):")
for i, val in zip(indices, I):
    print(f"  I[{i}] = {val:.6f}")
