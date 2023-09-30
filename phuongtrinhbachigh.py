a, b, c = map(int, input().split())
delta = b**2 - 4*a*c
if delta < 0 or a==0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    print("Phuong trinh co nghiem")
else:
    print("Phuong trinh co 2 nghiem phan biet")