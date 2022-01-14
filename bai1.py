# Bai 1
def square(n):
    square = {}
    for i in range(n+1):
        square[i] = i**2
    print(square)
    return square


n = int(input("Nhap vao n = "))

# a
name = "Lo Anh Tuan"
print(name)
n = len(name)
square(n)
