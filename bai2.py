ten = input(" Nhập tên đệm của bạn:  ")
print(ten)
n = len(ten)
def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
 
n = int(input("Tuan Anh thi n = "));
print("Tổng các chữ số của", n , "là", totalDigitsOfNumber(n));