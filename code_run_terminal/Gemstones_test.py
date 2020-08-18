k = eval(input("k : "))
list_rocks = []
i = 0
#Nhập rocks, cho vào list rocks dưới dạng set
while (i < k):
    rocks = set(input("Rock {} : ".format(i+1)))
    list_rocks.append(rocks)
    i+=1

print(list_rocks)

#Sử dụng hàm intersection với set, trả về các phần tử cùng xuất hiện trong các set thuộc list
gems = set.intersection(*list_rocks)
print(gems)
#Kết quả
print(len(gems))
