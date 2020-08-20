s = int(input())
list = []
k = 0
if 1<= s <= 150:
    for i in range(s):
        list.append(str(input()))
for v in list:
    if v == "++X" or v == "X++":
        k += 1
    elif v == "--X" or v == "X--":
        k -= 1
print (k)
# thuật toán:
# b1: nhập số nguyên s.
# b2: kiểm tra điều kiện 1<= s <=150:
# b3: nếu nằm trong khoảng thì thực hiện nhập các ký tự ở dòng 2 vào trong list.
# b4: kiểm tra các phần trong list:
#   - nếu phần tử đó là "X++" hoặc "++X" thì tăng biến k = 0 lên một đơn vị.
#   - nếu phần tử đó là "--X" hoặc "X--" thì giảm biến k đi 1 đơn vị. 
# b5: in ra kết quả.