import numpy as np #Phải pip install numpy trước


def __sum():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    sum = a + b
    print(sum)


def __matrix():

    # Tạo ma trận như đề
    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Tạo vector như đề
    v = np.array([1, 2, 3])

    # Tìm giới hạn và dạng của ma trận M
    rank_M = np.linalg.matrix_rank(M)
    shape_M = M.shape

    # Tìm dạng của vector
    shape_v = v.shape

    print("Giới hạn của ma trận M:", rank_M)
    print("Dạng của ma trận M:", shape_M)
    print("Dạng của vector V:", shape_v)

def new_matrix():


    #Tạo ma trận như câu trên
    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    #Tạo một ma trận mới với ma trận cũ cộng thêm 3
    new_matrix = M + 3

    print("Ma trận M:")
    print(M)

    print("\nMa trận mới sau khi cộng thêm 3:")
    print(new_matrix)

def transpose_matrix():
    # Tạo ma trận M
    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Tạo vector V
    v = np.array([1, 2, 3])

    # Chuyển đổi ma trận M
    M_transpose = np.transpose(M)

    # Chuyển đổi vector V
    v_transpose = np.transpose(v)

    print("Ma trận M:")
    print(M)

    print("\nBiến đổi ma trận M:")
    print(M_transpose)

    print("\nVector v:")
    print(v)

    print("\nBiến đổi vector v:")
    print(v_transpose)

if __name__ == '__main__':
    #__sum()
    #__matrix()
    #new_matrix()
    transpose_matrix()