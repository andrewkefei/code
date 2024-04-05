import numpy as np

def generate_random_matrix(rows, cols):
    return np.random.randint(1, 100, size=(rows, cols))  # 生成1到100之间的随机整数矩阵

# 生成一个3行3列的随机整数矩阵
rows = cols = 3
random_matrix = generate_random_matrix(rows, cols)
print(random_matrix)