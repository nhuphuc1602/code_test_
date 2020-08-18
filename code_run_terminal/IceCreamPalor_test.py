if __name__ == "__main__":
    i, j, k = 0, 0, 0
    cost_list = []
    money_pool = eval(input("Input money pool : ")) #Nhập tổng tiền 
    number_flavor = eval(input("Input number of flavors : ")) #Nhập số lượng kem

#Nhập giá tiền cho từng loại kem vào list
    while (k < number_flavor):
        cost_flavor = eval(input("Flavor {} : ".format(k+1)))
        cost_list.append(cost_flavor)
        k+=1
    print (cost_list)
    
#Sử dụng vòng lặp để duyệt list
    for i in range(i, len(cost_list)+1):
#Sử dụng vòng lặp thứ 2, duyệt từ i trở đi
        for j in range(i+1, len(cost_list)):
#Nếu tổng hai giá trị bằng money pool thì xuất i,j
            if (cost_list[i] + cost_list[j] == money_pool):
                print(i+1, j+1)
