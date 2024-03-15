
import math
import numpy as np
import matplotlib.pyplot as plt
def compute_norm(vector):
    norm = math.sqrt(sum([x**2 for x in vector]))
    return norm

def normalize_vector(vector):
    norm = compute_norm(vector)
    normalized_vector = [x / norm for x in vector]
    return normalized_vector

def Cau5():
    x = [3, 7]
    norm_x = compute_norm(x)
    print("Norm of x:", norm_x)
    normalized_x = normalize_vector(x)
    print("Normalized vector x:", normalized_x)


def vector_addition(a, b):
    return [x + y for x, y in zip(a, b)]


def vector_subtraction(a, b):
    return [x - y for x, y in zip(a, b)]


def Cau6():
    a = [10, 15]
    b = [8, 2]
    c = [1, 2, 3]
    sum_ab = vector_addition(a, b)
    print("a + b:", sum_ab)
    diff_ab = vector_subtraction(a, b)
    print("a - b:", diff_ab)
    diff_ac = vector_subtraction(a, c)
    print("a - c:", diff_ac)


def Cau7():
    a = [10, 15]
    b = [8, 2]
    dot_product = np.dot(a, b)
    print("Tích vô hướng của a và b:", dot_product)


def Cau8():
    A = np.array([[2, 4, 9], [3, 6, 7]])
    print(A)
    rank_A = np.linalg.matrix_rank(A)
    shape_A = A.shape
    print("Hạng của A:", rank_A)
    print("Dạng của A:", shape_A)
    value_7 = A[1, 2]
    print("Giá trị 7 trong A:", value_7)
    second_column = A[:, 1]
    print("Cột thứ 2 trong A:", second_column)


def Cau9():
    matrix = np.random.randint(-10, 10, (3, 3))
    print("Ma trận:")
    print(matrix)


def Cau10():
    identity_matrix = np.eye(3)
    print("Ma trận:")
    print(identity_matrix)


def Cau11():
    matrix = np.random.randint(1, 10, (3, 3))
    print("Ma trận:")
    print(matrix)
    trace_a = np.trace(matrix)
    print("Tổng đường chéo chính (A):", trace_a)
    trace_b = 0
    for i in range(3):
        trace_b += matrix[i][i]
    print("Tổng đường chéo chính (B):", trace_b)


def Cau12():
    diagonal_matrix = np.diag([1, 2, 3])
    print("Ma trận đường chéo:")
    print(diagonal_matrix)


def Cau13():
    A = np.array([[1, 1, 2], [2, 4, -3], [3, 6, -5]])
    print(A)
    determinant_A = np.linalg.det(A)
    print("Định thức của A:", determinant_A)


def Cau14():
    a1 = np.array([1, -2, -5])
    a2 = np.array([2, 5, 6])
    M = np.column_stack((a1, a2))
    print(M)


def Cau15():
    y = np.arange(-5, 6)
    y_squared = y ** 2
    plt.figure(figsize=(8, 6))
    plt.plot(y, y_squared, marker='o')
    plt.title('Đồ thị giá trị bình phương của y')
    plt.xlabel('y')
    plt.ylabel('y^2')
    plt.grid(True)
    plt.show()


def Cau16():
    values = np.linspace(0, 32, 4)
    print(values)


def Cau17():
    x = np.linspace(-5, 5, 50)
    y = x ** 2
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o')
    plt.title('Đồ thị y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def Cau18():
    x = np.linspace(-2, 2, 400)
    y = np.exp(x)
    plt.plot(x, y, label='y=exp(x)')
    plt.title('Plot of y=exp(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


def Cau19():
    x = np.linspace(0.01, 5, 400)
    y = np.log(x)
    plt.plot(x, y, label='y=log(x)')
    plt.title('Plot of y=log(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


def Cau20():
    x_exp = np.linspace(-2, 2, 400)
    x_log = np.linspace(0.01, 5, 400)
    y_exp = np.exp(x_exp)
    y_exp2 = np.exp(2 * x_exp)
    y_log = np.log(x_log)
    y_log2 = np.log(2 * x_log)
    fig, axs = plt.subplots(2)
    axs[0].plot(x_exp, y_exp, label='y=exp(x)')
    axs[0].plot(x_exp, y_exp2, label='y=exp(2x)')
    axs[0].set_title('Plot of y=exp(x) and y=exp(2x)')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')
    axs[0].legend()
    axs[1].plot(x_log, y_log, label='y=log(x)')
    axs[1].plot(x_log, y_log2, label='y=log(2x)')
    axs[1].set_title('Plot of y=log(x) and y=log(2x)')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('y')
    axs[1].legend()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    Cau5()
    Cau6()
    Cau7()
    Cau8()
    Cau9()
    Cau10()
    Cau11()
    Cau12()
    Cau13()
    Cau14()
    Cau15()
    Cau16()
    Cau17()
    Cau18()
    Cau19()
    Cau20()

