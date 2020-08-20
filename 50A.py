s = input()
lst = s.split(" ")
k = 0
if int(lst[1]) % 2 == 0:
    k = (int(lst[1]) / 2 ) * int(lst[0])
    print(int(k))
else:
    k = ((int(lst[1]) - 1) / 2 ) * int(lst[0]) + int(lst[0]) / 2
    print(int(k))

# input: chiều dài và chiều rộng của khung hcn.(m,n cùng trên 1 dòng cách nhau bằng khoảng trắng)
# output: số dominal cho vaog được trong khung hcn.  
# thuật toán.
    # b1: nhập chiều dài , chiều rộng.
    # b2: biến dòng vừa nhập thành 1 list sử dụng hàm split(" ").
    # b3: kiểm tra xem chiều dài của khung là só chẵn hay số lẻ.
    # b4: nếu chiều dài là chẵn: thì số dominal  = (chiều dài/2)*chiều rộng. sau đó in ra kết quả.
    # b5: nếu chiều dài là số lẻ: thì số dominal = ((chiều dài-1)/2)* chiều rộng + (chiều rộng/2). sau đó in ra kết quả.