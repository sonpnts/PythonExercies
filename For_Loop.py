def for_loop():
    name = input("Nhập tên của bạn: ")
    for c in name:
        print(c)



def odd_num():
    print("Tính tổng các số lẻ từ 1 đến 10")
    sum = 0
    for i in range(1 ,11):
        if (i % 2 != 0):
            print(i)
            sum+=i
    print(f'Tổng các số lẻ là: {sum}')


def Cau4():
    mydict = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4}
    #Print all key
    for key in mydict:
        print(key)

    #Print all value
    for value in mydict.values():
        print(value)

    #Print all key and value
    for key, value in mydict.items():
        print(key, value)


def Cau5():
    _num = []
    _course = []
    n = int(input("Nhap so luong phan tu trong mang: "))
    for i in range(1, n + 1):
        num = input(f"Nhap so thu {i}: ")
        _num.append(num)
        course = input(f"Nhap mon thu {i}: ")
        _course.append(course)
    data = list(zip(_num, _course))

    print(data)

def Cau6():

    c = input("Nhap vao 1 mang ki tu: ")
    print("FIND CONSONANTS")
    print("1. Without using 'Continue'")
    print("2. Using 'Continue'")
    choose = input("Lua chon cua ban: ")

    if choose == '1':
        print("-------------")
        consonant = "euoaiEUOAI"
        SumOfCons = 0
        for x in consonant:
            SumOfCons += c.count(x)
            c = c.replace(x, '$')
        print(f'Tong so nguyen am: {SumOfCons}')
        print(f'Chuoi sau khi cat nguyen am: {c}')
    if choose == '2':
        {}


def Cau7():
    x = -2
    y = 3

    while True:
        a = int(input("nhap a: "))

        if (a < x) | (a > y):
            print("Nhap sai, vui long nhap lai!!!")
        else:
            try:
                print(10 / a)
                break
            except ZeroDivisionError:
                print("Can't divided by zero!!!")

def Cau8():
    ages = [23, 10, 80]
    names = ['Hoa', 'Lam', 'Nam']

    # Combine ages and names into a list of tuples
    data = list(zip(ages, names))

    # Sort the list of tuples by increasing ages
    sorted_data = sorted(data, key=lambda x: x[0])

    print(sorted_data)

def Cau9():
    #Tạo file txt ở project trước
    input_file = open("firstname.txt")
    first_name = input_file.read()
    input_file.close()
    print(first_name)







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # for_loop()
    # odd_num()
    Cau4()
    #Cau5()
    #Cau6()
    #Cau7()
    #Cau8()
    #Cau9()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
