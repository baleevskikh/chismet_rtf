import numpy as np

x = np.array([1, 4, 5])
y = np.array([1, 64, 125])

# строим интерполяционный полином
coeffs = np.polyfit(x, y, 2)

# интеграл полинома
p = np.poly1d(coeffs)
P = np.polyint(p)

result = P(5) - P(1)

print(result)
