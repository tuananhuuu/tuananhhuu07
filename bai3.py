def thuan_nghich(n):
    m = n
    a = []
    while n!= 0:
        a.append(n % 10)
        n = n // 10
    a = ''.join(str(x) for x in a)
    if a == m:
        print(m, "la so thuan nghich")
    else:
        print(m, "khong la so thuan nghich")
thuan_nghich(1225)
