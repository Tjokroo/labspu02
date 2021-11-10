a=int(input("Masukan nilai pertama:"))
b=int(input("Masukan nilai kedua:"))
c=int(input("Masukan nilai ketiga:"))

if a>b and a>c:
    print(a,"Merupakan nilai terbesar")
elif b>a and b>c:
    print(b,"Merupakan nilai terbesar")
else:
    print(c,"Merupakan nilai terbesar")
