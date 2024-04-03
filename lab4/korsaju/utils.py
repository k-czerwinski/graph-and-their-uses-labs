import numpy as np

def dfs(adjency_matrix:np.matrix, d, f, n, time:int):
    d[n] = time
    for x, val in enumerate(adjency_matrix[n]):
        if val == 1 and d[x] == 0:
            time = dfs(adjency_matrix, d, f, x, time + 1)
    time = time + 1
    f[n] = time
    return f[n]

def dfs_2(adjency_matrix:np.matrix, components, n, component_num:int):
    components[n] = component_num
    for x, val in enumerate(adjency_matrix[n]):
        if val == 1 and components[x] == -1:
            dfs_2(adjency_matrix, components, x, component_num)
    return component_num

def korsaju(adjency_matrix:np.matrix):
    n = len(adjency_matrix)
    d = np.zeros(n)
    f = np.zeros(n)
    time = 0
    for i in range(n):
        if d[i] == 0:
            time = dfs(adjency_matrix, d, f, i, time + 1)
    adjency_matrix_transposed = adjency_matrix.transpose()
    f_with_v_index = tuple((value, index) for index, value in enumerate(f))
    f_with_v_index_sorted = sorted(f_with_v_index, key=lambda x: x[0], reverse=True)
    components = [-1 for _ in range(n)]
    component_num = 0
    for i in range(n):
        if components[f_with_v_index_sorted[i][1]] == -1:
            component_num = dfs_2(adjency_matrix_transposed, components, f_with_v_index_sorted[i][1], component_num + 1)
    return components


